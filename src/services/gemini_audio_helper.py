import logging

from fastapi import HTTPException, UploadFile
from fastapi.concurrency import run_in_threadpool
from google import genai
from google.genai.errors import APIError, ClientError

from src.services.audio_ai_service_base import AudioAIService

logger = logging.getLogger(__name__)


class GeminiAudioService(AudioAIService):
    def __init__(self, client: genai.Client, model_name: str, prompt: str) -> None:
        super().__init__(client=client, prompt=prompt)
        self._model_name = model_name

    def _upload_audio_to_genai(self, input_file: UploadFile):
        try:
            return self._client.files.upload(
                file=input_file.file,
                config={"mime_type": input_file.content_type},
            )
        except ClientError as e:
            logger.exception("Client error while uploading file to Gemini")
            raise HTTPException(
                status_code=400, detail=f"Invalid request to GenAI: {str(e)}"
            )
        except APIError as e:
            logger.exception("Gemini API error during file upload")
            raise HTTPException(
                status_code=502,
                detail=f"GenAI service is temporarily unavailable: {str(e)}",
            )
        except Exception as e:
            logger.exception("Unexpected error during file upload")
            raise HTTPException(
                status_code=500,
                detail=f"Internal server error during file upload: {str(e)}",
            )

    async def generate_answer_from_audio(self, input_file) -> str:
        try:
            uploaded_file = self._upload_audio_to_genai(input_file)
            response = await run_in_threadpool(
                self._client.models.generate_content,
                model=self._model_name,
                contents=[
                    self._prompt,
                    uploaded_file,
                ],
            )
            if not response or not response.text:
                raise HTTPException(
                    status_code=502, detail="GenAI returned an empty response"
                )
            return response.text
        except APIError as e:
            logger.exception("Gemini API error during generation")
            raise HTTPException(
                status_code=502, detail=f"GenAI failed to process the audio: {str(e)}"
            )
        except Exception as e:
            logger.exception("Unexpected error during content generation")
            raise HTTPException(
                status_code=500,
                detail=f"Internal server error during AI processing: {str(e)}",
            )

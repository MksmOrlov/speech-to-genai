import uvicorn
from fastapi import Depends, FastAPI, File, UploadFile

from src.dependencies import get_audio_service
from src.services.audio_ai_service_base import AudioAIService
from src.services.audio_validator import AudioValidator

app = FastAPI()


@app.post("/process-voice/")
async def voice_to_answer(
    file: UploadFile = File(..., description="Request audio file"),
    gemini_audio_helper: AudioAIService = Depends(get_audio_service),
):
    AudioValidator().validate(file)
    answer = await gemini_audio_helper.generate_answer_from_audio(file)

    return {"answer": answer}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000)

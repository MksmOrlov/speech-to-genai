import uvicorn
from fastapi import Depends, FastAPI, File, UploadFile

from dependencies import get_audio_service
from services.audio_ai_service_base import AudioAIService
from services.audio_validator import AudioValidator

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
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

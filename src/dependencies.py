from google import genai

from config import settings
from services.gemini_audio_helper import GeminiAudioService
from services.audio_ai_service_base import AudioAIService


def get_audio_service() -> AudioAIService:
    client = genai.Client(api_key=settings.gemini_api_key)
    return GeminiAudioService(client, settings.gemini_model, settings.gemini_prompt)

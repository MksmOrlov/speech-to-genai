from google import genai

from src.config import settings
from src.services.gemini_audio_helper import GeminiAudioService
from src.services.audio_ai_service_base import AudioAIService


def get_audio_service() -> AudioAIService:
    client = genai.Client(api_key=settings.gemini_api_key)
    return GeminiAudioService(client, settings.gemini_model, settings.gemini_prompt)

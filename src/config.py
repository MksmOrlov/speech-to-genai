from pydantic_settings import BaseSettings, SettingsConfigDict


class GeminiSettings(BaseSettings):
    gemini_api_key: str
    gemini_model: str = "gemini-3-flash-preview"
    gemini_prompt: str = "Преобразуй голос в текст и ответь по смыслу"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")


settings = GeminiSettings()

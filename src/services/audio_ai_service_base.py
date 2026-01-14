from abc import ABC, abstractmethod


class AudioAIService(ABC):
    """
    Extandable class for GenAI audio services.
    """

    def __init__(self, client, prompt: str) -> None:
        self._client = client
        self._prompt = prompt

    @abstractmethod
    async def generate_answer_from_audio(self, audio_file) -> str:
        raise NotImplementedError

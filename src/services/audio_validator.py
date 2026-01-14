from fastapi import HTTPException, UploadFile


class AudioValidator:
    """
    Extendable audio file validator. Here you can add more validation rules if needed.
    """

    ALLOWED_MIME_PREFIX = "audio/"

    @classmethod
    def validate(cls, audio_file: UploadFile) -> None:
        if not audio_file:
            raise HTTPException(status_code=400, detail="Audio file is required")

        if not audio_file.content_type:
            raise HTTPException(status_code=400, detail="Unknown file content type")

        if not audio_file.content_type.startswith(cls.ALLOWED_MIME_PREFIX):
            raise HTTPException(
                status_code=400,
                detail="File is not an audio format",
            )

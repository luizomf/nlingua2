# pyright: basic
from io import StringIO
from pathlib import Path

import whisper
from whisper.tokenizer import LANGUAGES, TO_LANGUAGE_CODE
from whisper.utils import WriteSRT

WHISPER_MODEL_NAME = "turbo"
WHISPER_LANGUAGES_BY_NAME: dict[str, str] = TO_LANGUAGE_CODE
WHISPER_LANGUAGES_BY_CODE: dict[str, str] = LANGUAGES


class SRTStringWriter(WriteSRT):
    def __init__(self) -> None:
        super().__init__("")

    def write_result(self, result: dict) -> str:
        s = StringIO()
        super().write_result(result, file=s)
        return s.getvalue().strip()


def transcribe_file_to_srt_string(input_path: Path, language: str = "pt") -> str:
    model = whisper.load_model(WHISPER_MODEL_NAME)
    result = model.transcribe(
        str(input_path), language=language, task="transcribe", verbose=True
    )
    return SRTStringWriter().write_result(result)

from pathlib import Path

from nlingua2.exceptions import InvalidLanguageError
from nlingua2.models import TranslateFileToFileParams
from nlingua2.settings import WHISPER_AND_NLLB_LANGUAGES


def validate_input_file(path: Path) -> None:
    if not path.exists():
        msg = f"Input file not found: {path}"
        raise FileNotFoundError(msg)


def validate_output_file(path: Path) -> None:
    if not path.parent.exists():
        msg = f"Directory '{path.parent}' does not exist."
        raise FileNotFoundError(msg)
    if path.exists():
        msg = f"Output file already exists: {path}"
        raise FileExistsError(msg)


def validate_nllb_language(lang: str) -> None:
    if lang not in WHISPER_AND_NLLB_LANGUAGES:
        msg = (
            f"Invalid NLLB language: {lang}. "
            "Use `nlingua2 nllb_languages` to see available languages."
        )
        raise InvalidLanguageError(msg)


def validate_whisper_language(lang: str) -> None:
    if lang not in WHISPER_AND_NLLB_LANGUAGES:
        msg = (
            f"Invalid Whisper language: {lang}. "
            "Use `nlingua2 whisper_languages` to see available languages."
        )
        raise InvalidLanguageError(msg)


def validate_from_file_to_file(
    args: TranslateFileToFileParams,
) -> None:
    validate_input_file(args.input)

    if not args.force:
        validate_output_file(args.output)

    validate_nllb_language(args.src_lang)
    validate_nllb_language(args.tgt_lang)


def validate_transcribe_to_file(
    input_path: Path, output_path: Path, src_lang: str, *, force: bool = False
) -> None:
    validate_input_file(input_path)

    if not force:
        validate_output_file(output_path)

    validate_whisper_language(src_lang)

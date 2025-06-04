from pathlib import Path

from nlingua2.models import SubRipEntry, TranslateFileToFileParams
from nlingua2.parser import (
    read_subrip_file,
    subrip_entries_to_file,
    subrip_entries_to_str,
    subrip_text_to_entries,
    translate_subrip_entries,
    write_subrip_file,
)
from nlingua2.settings import SUBRIP_DIR, WHISPER_AND_NLLB_LANGUAGES
from nlingua2.validation import validate_from_file_to_file, validate_transcribe_to_file
from nlingua2.whisperer import transcribe_file_to_srt_string


def translate_entries(
    text: str,
    src_lang: str,
    tgt_lang: str,
) -> list[SubRipEntry]:
    entries = subrip_text_to_entries(text)
    return translate_subrip_entries(entries, src_lang, tgt_lang)


def translate_from_file_to_file(params: TranslateFileToFileParams) -> None:
    input_path = params.input
    output_path = params.output
    src_lang = params.src_lang
    tgt_lang = params.tgt_lang

    validate_from_file_to_file(params)

    nllb_src_lang = WHISPER_AND_NLLB_LANGUAGES[src_lang]["nllb"]
    nllb_tgt_lang = WHISPER_AND_NLLB_LANGUAGES[tgt_lang]["nllb"]

    text = read_subrip_file(input_path)
    entries = translate_entries(text, nllb_src_lang, nllb_tgt_lang)
    subrip_entries_to_file(entries, output_path)

    print(f"📥 Input:  {input_path}")
    print(f"📤 Output: {output_path}\n")


def transcribe_from_file_to_file(
    input_path: Path, output_path: Path, src_lang: str, *, force: bool = False
) -> None:
    validate_transcribe_to_file(input_path, output_path, src_lang, force=force)
    whisper_src_lang = WHISPER_AND_NLLB_LANGUAGES[src_lang]["whisper"]

    srt = transcribe_file_to_srt_string(input_path, language=whisper_src_lang)
    write_subrip_file(output_path, srt)

    print("\n🟢 Done! Transcription complete.\n")

    print(f"📥 Input:  {input_path}")
    print(f"📤 Output: {output_path}\n")


def run() -> None:
    input_path = SUBRIP_DIR / "aula.srt"
    subrip_from_file = read_subrip_file(input_path)
    subrip_entries = subrip_text_to_entries(subrip_from_file)
    subrip_str = subrip_entries_to_str(subrip_entries)

    print(subrip_str)
    print()

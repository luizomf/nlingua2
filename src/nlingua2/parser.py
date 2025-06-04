from pathlib import Path

from nlingua2.exceptions import SubRipNotValidException
from nlingua2.factories import create_subrip_entry
from nlingua2.models import SubRipEntry
from nlingua2.translator import translate
from nlingua2.utils import DOUBLE_EOL_RE, EOL_RE


def subrip_text_to_entries(subrip: str) -> list[SubRipEntry]:
    if not subrip.strip():
        msg = "Input .srt file is empty or only whitespace."
        raise SubRipNotValidException(msg)

    subrip_entry_lines = DOUBLE_EOL_RE.split(subrip)
    entries: list[SubRipEntry] = []

    for entry_line in subrip_entry_lines:
        parsed_entry = parse_subrip_entry(entry_line)

        if not parsed_entry:
            continue

        entry_sequence, entry_timecodes, entry_text_lines = parsed_entry
        entry = create_subrip_entry(
            entry_sequence,
            entry_timecodes,
            entry_text_lines,
        )
        entries.append(entry)

    return entries


def translate_subrip_entries(
    entries: list[SubRipEntry],
    src_lang: str = "por_Latn",
    tgt_lang: str = "eng_Latn",
) -> list[SubRipEntry]:
    translated_entries: list[SubRipEntry] = []

    total = len(entries)
    for idx, entry in enumerate(entries, start=1):
        print(f"🎬 Traduzindo {idx}/{total}")
        print(f"🗣️  Texto original: {entry.full_sentence.strip()}")

        translated_sentences: list[str] = []
        for sentence in entry.sentences:
            translated = translate(sentence, src_lang, tgt_lang)
            translated_sentences.append(translated)

        print(f"🌍 Texto traduzido: {' '.join(translated_sentences).strip()}")
        print("—" * 60)  # linha separadora
        print()

        translated_entry = SubRipEntry(
            sequence=entry.sequence,
            start=entry.start,
            end=entry.end,
            sentences=translated_sentences,
            char_count=len("".join(translated_sentences)),
            word_count=sum(len(s.split()) for s in translated_sentences),
        )
        translated_entries.append(translated_entry)

    print("\n🟢 Done! Translation complete.\n")
    return translated_entries


def subrip_entries_to_str(subrip_entries: list[SubRipEntry]) -> str:
    subrip_str = ""
    for sentence in subrip_entries:
        subrip_str += f"{sentence.sequence}\n"
        subrip_str += f"{sentence.start} --> {sentence.end}\n"

        for text_line in sentence.sentences:
            subrip_str += f"{text_line}\n"

        subrip_str += "\n"
    return subrip_str.strip()


def subrip_entries_to_file(
    subrip_entries: list[SubRipEntry],
    output_path: Path,
) -> str:
    subrip_str = subrip_entries_to_str(subrip_entries)
    write_subrip_file(output_path, subrip_str)
    return subrip_str


def read_subrip_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()


def write_subrip_file(path: Path, file_content: str) -> None:
    with path.open("w", encoding="utf-8") as file:
        file.write(file_content)


def parse_subrip_entry(block: str) -> tuple[str, str, list[str]] | None:
    lines = EOL_RE.split(block)

    if len(lines) < 2:
        msg = "Bloco subrip malformado."
        print(msg)
        return None

    sequence_line, timecodes_line, *text_lines = lines
    return sequence_line, timecodes_line, text_lines

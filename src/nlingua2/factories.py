from unicodedata import normalize

from nlingua2.models import SubRipEntry
from nlingua2.translator import translate
from nlingua2.utils import get_subrip_timecodes_or_fail


def create_subrip_entry(
    sequence: str,
    timecodes_text: str,
    text_lines: list[str],
) -> SubRipEntry:
    text_lines = [line.strip() for line in text_lines if line.strip()]

    timecodes = get_subrip_timecodes_or_fail(timecodes_text)
    start, end = timecodes

    char_count = len("".join(text_lines))
    word_count = sum(len(line.strip().split()) for line in text_lines)

    return SubRipEntry(
        sequence=normalize("NFC", sequence),
        start=start,
        end=end,
        sentences=text_lines,
        char_count=char_count,
        word_count=word_count,
    )


def create_translated_subrip_entries(
    original_entries: list[SubRipEntry],
) -> list[SubRipEntry]:
    translated_entries: list[SubRipEntry] = []

    for original in original_entries:
        translated = translate(original.sequence)
        entry = SubRipEntry(
            sequence=original.sequence,
            start=original.start,
            end=original.end,
            sentences=[translated],
            char_count=len(translated),
            word_count=len(translated.split()),
        )
        translated_entries.append(entry)

    return translated_entries

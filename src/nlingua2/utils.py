import re

from nlingua2.exceptions import TimecodeError
from nlingua2.settings import WHISPER_AND_NLLB_LANGUAGES

TIMECODE_RE = re.compile(
    r"^(\d{2}:\d{2}:\d{2},\d{3})\s-->\s(\d{2}:\d{2}:\d{2},\d{3})$",
)
EOL_PATTERN = r"(?:\r?\n)"
EOL_RE = re.compile(EOL_PATTERN)
DOUBLE_EOL_RE = re.compile(f"{EOL_PATTERN}{{2}}")

SENTENCE_END_RE = re.compile(r"[\.\?\!](?=\s|\Z)")


def get_subrip_timecodes_or_fail(text: str) -> tuple[str, str]:
    matches = TIMECODE_RE.match(text)

    if matches is None:
        msg = f"Invalid timecodes for: {text}"
        raise TimecodeError(msg)

    return matches.group(1), matches.group(2)


def print_languages() -> None:
    print("\nAvailable Languages:\n")

    for code, name in WHISPER_AND_NLLB_LANGUAGES.items():
        print(f"{code} = {name.get('label')}")

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class SubRipEntry:
    sequence: str
    start: str
    end: str
    sentences: list[str]
    char_count: int
    word_count: int

    @property
    def full_sentence(self) -> str:
        return " ".join(self.sentences).strip()


@dataclass
class SubRipToSentence:
    complete_sentence: str
    sequences: list[int]
    original_entries: list[SubRipEntry] = field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]


@dataclass
class TranslateFileToFileParams:
    input: Path
    output: Path
    src_lang: str
    tgt_lang: str
    force: bool

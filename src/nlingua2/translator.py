# pyright: basic
from typing import cast

from typing_extensions import TypedDict

_cached_translators = {}


class TranslationOutput(TypedDict):
    translation_text: str


def get_translator(src_lang: str, tgt_lang: str):  # noqa
    from transformers.pipelines import pipeline

    key = f"{src_lang}->{tgt_lang}"
    if key not in _cached_translators:
        _cached_translators[key] = pipeline(
            "translation",
            model="facebook/nllb-200-distilled-600M",
            src_lang=src_lang,
            tgt_lang=tgt_lang,
            max_length=512,
        )
    return _cached_translators[key]


def translate(
    text: str,
    src_lang: str = "por_Latn",
    tgt_lang: str = "eng_Latn",
) -> str:
    translator = get_translator(src_lang, tgt_lang)
    result = translator(text, max_new_tokens=256, num_beams=4, do_sample=False)

    output = cast("list[TranslationOutput]", result)
    return output[0]["translation_text"]

import argparse
import sys
from pathlib import Path

from nlingua2.exceptions import (
    InvalidLanguageError,
    SubRipNotValidError,
    TimecodeError,
)
from nlingua2.models import TranslateFileToFileParams
from nlingua2.runner import transcribe_from_file_to_file, translate_from_file_to_file
from nlingua2.utils import print_languages

CMD_TRANSLATE = "translate"
CMD_TRANSCRIBE = "transcribe"
CMD_SHOW_LANGUAGES = "show_languages"


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="nlingua2 - Any Language to Any Language",
        description=(
            "CLI for transcribing audio/video with Whisper and "
            "translating/rebuilding SRT subtitles using Hugging Face "
            "NLLB models."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command")

    translate_parser = subparsers.add_parser(
        CMD_TRANSLATE,
        help="Translate subrip (srt) files",
    )

    translate_parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Full path to the input .srt file with extension",
    )
    translate_parser.add_argument(
        "--from",
        "-f",
        dest="src_lang",
        required=True,
        help=(
            f"Source language (e.g., english). Use `nlingua2 {CMD_SHOW_LANGUAGES}` "
            "to see all available languages."
        ),
    )

    translate_parser.add_argument(
        "--to",
        "-t",
        dest="tgt_lang",
        required=True,
        help=f"Target language (e.g., english). Use `nlingua2 {CMD_SHOW_LANGUAGES}` to see all available languages.",  # noqa: E501
    )
    translate_parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Full path to the output .srt file with extension",
    )
    translate_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite output file if it already exists",
    )

    transcribe_parser = subparsers.add_parser(
        CMD_TRANSCRIBE,
        help="Transcribe audio or video files",
    )

    transcribe_parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Full path to the input video file with extension",
    )
    transcribe_parser.add_argument(
        "--from",
        "-f",
        dest="src_lang",
        required=True,
        help=f"Source language (e.g., english). Use `nlingua2 {CMD_SHOW_LANGUAGES}` to see all available languages.",  # noqa: E501
    )
    transcribe_parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Full path to the output SRT file with extension",
    )
    transcribe_parser.add_argument(
        "--translate_srt_to",
        help=f"Target language to translate the SRT File (e.g., english). Use `nlingua2 {CMD_SHOW_LANGUAGES}` to see all available languages.",  # noqa: E501
    )
    transcribe_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite output file if it already exists",
    )

    subparsers.add_parser(
        CMD_SHOW_LANGUAGES,
        help="Show all supported languages",
    )

    args = parser.parse_args()

    try:
        if args.command == CMD_SHOW_LANGUAGES:
            print_languages()
        elif args.command == CMD_TRANSLATE:
            params = TranslateFileToFileParams(
                Path(args.input).resolve(),
                Path(args.output).resolve(),
                args.src_lang,
                args.tgt_lang,
                args.force,
            )
            translate_from_file_to_file(
                params,
            )
        elif args.command == CMD_TRANSCRIBE:
            input_path = Path(args.input).resolve()
            output_path = Path(args.output).resolve()

            transcribe_from_file_to_file(
                input_path,
                output_path,
                args.src_lang,
                force=args.force,
            )

            if args.translate_srt_to:
                translate_srt_to_path = output_path.with_name(
                    f"{output_path.stem}-{args.translate_srt_to}{output_path.suffix}"
                )

                params = TranslateFileToFileParams(
                    output_path,
                    translate_srt_to_path,
                    args.src_lang,
                    args.translate_srt_to,
                    args.force,
                )
                translate_from_file_to_file(
                    params,
                )
        else:
            parser.print_help()
    except (SubRipNotValidError, TimecodeError) as e:
        print(f"\n🔴 Error with SRT file: {e}\n")
        sys.exit(2)
    except InvalidLanguageError as e:
        print(f"\n🔴 Language error: {e}\n")
        sys.exit(3)
    except (FileNotFoundError, FileExistsError) as e:
        print(f"\n🔴 File error: {e}\n")
        sys.exit(4)
    except RuntimeError as e:
        print(f"\n🔴 File not valid: {e.__class__.__name__}: {e}\n")
        sys.exit(5)


if __name__ == "__main__":
    main()

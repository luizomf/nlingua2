import argparse
import sys
from pathlib import Path


class BGColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def print_error(error: str) -> None:
    print("\n🔴", f"{BGColors.FAIL}{error}{BGColors.ENDC}\n")


def print_success(msg: str) -> None:
    print("\n🟢", f"{BGColors.OKGREEN}{msg}{BGColors.ENDC}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Code Reader",
        description="Read code files",
    )

    parser.add_argument(
        "-p",
        "--path",
        default=".",
        help="Path to the folder to read files from",
    )

    parser.add_argument(
        "-g",
        "--glob",
        required=True,
        help="Glob pattern matching",
    )

    parser.add_argument(
        "-e",
        "--exclude",
        nargs="+",
        required=True,
        help="Files to exclude.",
    )

    args = parser.parse_args()

    path = Path(args.path).resolve()
    glob_pattern = args.glob
    exclude = args.exclude

    if not path.exists() or not path.is_dir():
        print_error("Path does not exist or is not a directory.")
        sys.exit(1)

    for file in path.glob(glob_pattern):
        should_exclude = [part for part in file.parts if part in exclude]

        if should_exclude or not file.is_file():
            continue

        print_success(str(file))

        print(file.read_text())


if __name__ == "__main__":
    main()

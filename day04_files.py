"""
Day 04 - File Utilities
"""

from pathlib import Path


def read_text_file(file_path: str) -> str:
    """Read and return contents of a text file."""
    return Path(file_path).read_text(encoding="utf-8")


def write_text_file(file_path: str, content: str) -> None:
    """Write text content to a file."""
    Path(file_path).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    sample_path = "sample.txt"
    write_text_file(sample_path, "Hello, Day 4!")
    print(read_text_file(sample_path))

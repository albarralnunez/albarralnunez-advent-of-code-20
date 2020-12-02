from pathlib import Path
from typing import Iterator, Optional
import re

from models import Password


password_regex = re.compile("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")


def build_password(line: str) -> Optional[Password]:
    password_match = password_regex.match(line)
    if not password_match:
        return None
    return Password(
        min=int(password_match.group(1)),
        max=int(password_match.group(2)),
        letter=password_match.group(3),
        value=password_match.group(4),
    )


def read_input(input_file_path: str) -> Iterator[Password]:
    """
    10-11 g: jdgggcctgsg
    """
    with Path(input_file_path).open() as input:
        return filter(None, map(build_password, input.read().splitlines()))

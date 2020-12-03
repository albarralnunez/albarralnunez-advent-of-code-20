import operator
import re
from functools import reduce
from pathlib import Path
from typing import Iterator, List, Optional

password_regex = re.compile("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")


def read_input(input_file_path: str) -> List[str]:
    """
    10-11 g: jdgggcctgsg
    """
    with Path(input_file_path).open() as input:
        return input.read().splitlines()

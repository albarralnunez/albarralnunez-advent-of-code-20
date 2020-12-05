import operator
import re
from functools import reduce
from pathlib import Path
from typing import Iterator, List, Optional


def read_input(input_file_path: str) -> List[str]:
    with Path(input_file_path).open() as input:
        return input.read().splitlines()

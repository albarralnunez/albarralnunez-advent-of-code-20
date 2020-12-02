from typing import Iterable, Iterator
import operator
from functools import reduce
from pathlib import Path


def read_input(input_file_path: str) -> Iterator[int]:
    with Path(input_file_path).open() as input:
        return map(int, input.read().splitlines())


def prod(numbers: Iterable[int]) -> int:
    return reduce(operator.mul, numbers, 1)

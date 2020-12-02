from typing import Iterable
import operator
from functools import reduce
from pathlib import Path


def read_input(input_file_path: str) -> Iterable[int]:
    with Path(input_file_path).open() as input:
        return map(int, input.read().splitlines())

def prod(numbers: Iterable[int]):
    return reduce(operator.mul, numbers, 1)

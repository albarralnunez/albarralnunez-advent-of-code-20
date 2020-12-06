import operator
import re
from functools import reduce
from pathlib import Path
from typing import Callable, Iterator, List, Optional, Set


def read_input(input_file_path: str) -> str:
    with Path(input_file_path).open() as input:
        return input.read()


def split_to_sets(x: str) -> Iterator[Set]:
    return map(set, x.split())


def reduce_group(group: Iterator[Set], operation) -> Set[str]:
    return reduce(lambda x, y: operation(x, y), group)


def process_input(input_str: str, operation: Callable) -> int:
    groups: List[str] = input_str.split("\n\n")
    groups_passangers: Iterator[Iterator[Set[str]]] = map(split_to_sets, groups)
    group_answers = map(lambda x: reduce_group(x, operation), groups_passangers)
    return sum(map(len, group_answers))


def main():
    poll = read_input("./input.txt")
    print(f"Solution 1: {process_input(poll, operator.__or__)}")
    print(f"Solution 2: {process_input(poll, operator.__and__)}")


if __name__ == "__main__":
    main()

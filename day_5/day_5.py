import math
from itertools import dropwhile, product
from typing import Callable, List, Set, Tuple

from utils import read_input

rows_navigation: int = 7
num_rows: int = 128
coloumns_navigation: int = 3
num_coloumns: int = 8


def calculator(
    letters: str, navigation: int, letter: str, num: int, round: Callable
) -> int:
    return round(
        sum(
            map(
                lambda x: x[1],
                filter(
                    lambda x: letter == x[0],
                    zip(
                        letters,
                        map(
                            lambda x: x[0] / x[1],
                            zip(
                                [num] * navigation,
                                map(
                                    lambda x: x[0] ** x[1],
                                    zip([2] * navigation, range(1, navigation + 1)),
                                ),
                            ),
                        ),
                    ),
                ),
            )
        )
    )


def get_row(letters: str) -> int:
    return calculator(
        letters=letters,
        navigation=rows_navigation,
        letter="B",
        num=num_rows,
        round=round,
    )


def get_coloumn(
    letters: str,
) -> int:
    return calculator(
        letters=letters,
        navigation=coloumns_navigation,
        letter="R",
        num=num_coloumns,
        round=math.ceil,
    )


def get_position(ticket: str) -> Tuple[int, int]:
    row: str = ticket[:rows_navigation]
    coloumn: str = ticket[-coloumns_navigation:]
    row_calculator = get_row(letters=row)
    coloumn_calculator = get_coloumn(letters=coloumn)
    return (int(row_calculator), int(coloumn_calculator))


def get_id(x, y) -> int:
    return x * 8 + y


def get_all_ids(tickets):
    return map(lambda x: get_id(*x), map(get_position, tickets))


def is_valid(element, elements):
    return element - 1 in elements and element + 1 in elements


def solution_1(tickets) -> int:
    return max(get_all_ids(tickets))


def solution_2(tickets) -> int:
    all_ids: Set[int] = set(
        map(lambda x: get_id(*x), product(range(0, num_rows), range(0, num_coloumns)))
    )
    list_ids: Set[int] = set(get_all_ids(tickets))
    possible_results = all_ids - list_ids
    return next(
        dropwhile(
            lambda x: not x[0],
            map(lambda x: (is_valid(x, list_ids), x), possible_results),
        )
    )[1]


def main():
    tickets = read_input("./input_1.txt")
    print(f"Solution 1: {solution_1(tickets)}")
    tickets = read_input("./input_2.txt")
    print(f"Solution 1: {solution_2(tickets)}")


if __name__ == "__main__":
    main()

from typing import Iterable, Tuple
from itertools import combinations, dropwhile
from functools import reduce

from utils import prod, read_input


def solution(entries: Iterable[int], number_of_combinations: int): 
    filter_numbers: Iterable[int] = filter(lambda entry: entry < 2020, entries)
    combinations_of_numbers: Iterable[Tuple[int, int]] = combinations(
       filter_numbers, number_of_combinations
    )
    sum_of_combinations: Iterable[Tuple[int, int]] = map(
        lambda x: (sum(x), prod(x)), combinations_of_numbers
    )
    find_solution: Iterable[Tuple[int, int]] = dropwhile(
        lambda x: x[0] != 2020, sum_of_combinations
    )
    result = next(find_solution)
    return result[1]


def main():
    entries_1: Iterable[int] = read_input("./input_1.txt")
    print(f"Solution 1: {solution(entries_1, 2)}")
    entries_2: Iterable[int] = read_input("./input_2.txt")
    print(f"Solution 2: {solution(entries_2, 3)}")

if __name__ == '__main__':
    main()




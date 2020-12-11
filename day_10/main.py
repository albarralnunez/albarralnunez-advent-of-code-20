from itertools import chain, groupby
from math import prod
from pathlib import Path
from typing import Iterator, List, Tuple

JoltageRating = int
JoltageDifference = int
Bag = List[JoltageRating]


aux_combinations = {2: 2, 3: 4, 4: 7}


def read_input(file_path: str) -> Bag:
    with Path(file_path).open() as input:
        return list(chain([0], map(int, input.read().splitlines())))


def generate_adapters_differences(adapters: Bag):
    sorted_adapters: List[Tuple[int, JoltageRating]] = list(enumerate(sorted(adapters)))
    grouped_adapters: List[Tuple[JoltageRating, JoltageRating]] = list(
        map(lambda x: (x[1], sorted_adapters[x[0] + 1][1]), sorted_adapters[:-1])
    )
    adapters_differences: List[JoltageDifference] = list(
        map(lambda x: x[1] - x[0], grouped_adapters)
    )
    return adapters_differences


def problem_1(adapters: Bag):
    adapters_differences: List[JoltageDifference] = generate_adapters_differences(
        adapters
    )
    differences_3_jolds: List[JoltageDifference] = list(
        filter(lambda x: x == 3, adapters_differences)
    )
    differences_1_jolds: List[JoltageDifference] = list(
        filter(lambda x: x == 1, adapters_differences)
    )
    return len(differences_1_jolds) * (len(differences_3_jolds) + 1)


def problem_2(adapters: Bag):
    adapters_differences: List[JoltageDifference] = generate_adapters_differences(
        adapters
    )
    groups_of_ones: Iterator[Tuple[int, Iterator]] = filter(
        lambda x: x[0] == 1, groupby(adapters_differences)
    )
    len_groups_of_ones: Iterator[int] = map(lambda x: len(list(x[1])), groups_of_ones)
    # print(list(len_groups_of_ones))
    possible_combinations: Iterator[int] = map(
        lambda x: aux_combinations[x], filter(lambda x: x != 1, len_groups_of_ones)
    )
    # print(list(possible_combinations))
    result = prod(possible_combinations)
    return result


def main():
    input_test_1 = read_input("./input_test_1.txt")
    input_test_2 = read_input("./input_test_2.txt")
    input_problem = read_input("./input.txt")
    print(f"Solution Test 1 Problem 1: {problem_1(input_test_1)}")
    print(f"Solution Test 2 Problem 1: {problem_1(input_test_2)}")
    print(f"Solution Problem 1: {problem_1(input_problem)}")
    print(f"Solution Test 1 Problem 2: {problem_2(input_test_1)}")
    print(f"Solution Test 2 Problem 2: {problem_2(input_test_2)}")
    print(f"Solution Problem 2: {problem_2(input_problem)}")


if __name__ == "__main__":
    main()

from itertools import combinations, dropwhile
from pathlib import Path
from typing import Generator, List, Optional


def read_rules(input_file_path: str) -> List[int]:
    with Path(input_file_path).open() as input:
        return list(map(int, input.read().splitlines()))


def is_valid_sequence(permable_group: List[int], permable: int):
    for_validation, validate = permable_group[:permable], permable_group[-1]
    is_valid = any(
        map(lambda x: x == validate, map(sum, combinations(for_validation, 2)))
    )
    return is_valid


def matches_target_candidates_generator(
    sequence: List[int], target: int, position: int = 0, group_size: int = 2
) -> Generator[List[int], List[int], None]:
    sub_sequence = sequence[position : position + group_size]
    while sum(sub_sequence) != target:
        if sum(sub_sequence) > target:
            position += 1
            group_size = 2
            sub_sequence = sequence[position : position + group_size]
        yield sub_sequence
        group_size += 1
        sub_sequence = sequence[position : position + group_size]
    yield sub_sequence


def problem_1(sequence: List[int], permable: int):
    groups = filter(
        lambda x: len(x) >= permable,
        [
            sequence[position : position + permable + 1]
            for position in range(len(sequence))
        ],
    )
    result = dropwhile(lambda x: is_valid_sequence(x, permable), groups)
    return list(next(result))[-1]


def problem_2(sequence, target):
    *_, result = matches_target_candidates_generator(sequence, target)
    return min(result) + max(result)


def main():
    sequence_test = read_rules("./input_test.txt")
    solution_1_test = problem_1(sequence_test, 5)
    print(f"Test 1: {solution_1_test}")
    sequence = read_rules("./input.txt")
    solution_1 = problem_1(sequence, 25)
    print(f"Solution 1: {solution_1}")
    solution_2_test = problem_2(sequence_test, solution_1_test)
    print(f"Test 2: {solution_2_test}")
    solution_2 = problem_2(sequence, solution_1)
    print(f"Solution 2: {solution_2}")


if __name__ == "__main__":
    main()

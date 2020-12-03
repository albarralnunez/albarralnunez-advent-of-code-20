from typing import Iterator

from utils import prod, read_input


def navigate(step_x, step_y, slope):
    trees = 0
    row = 0
    coloumn = 0
    while True:
        if slope[row][coloumn] == "#":
            trees += 1
        row += step_y
        if row >= len(slope):
            break
        coloumn += step_x
        coloumn %= len(slope[row])
    return trees


def solution_1(slope):
    return navigate(3, 1, slope)


def solution_2(slope):
    results = [
        navigate(1, 1, slope),
        navigate(3, 1, slope),
        navigate(5, 1, slope),
        navigate(7, 1, slope),
        navigate(1, 2, slope),
    ]
    return prod(results)


def main():
    input_1 = read_input("./input_1.txt")
    print(f"Solution 1: {solution_1(input_1)}")
    input_2 = read_input("./input_2.txt")
    print(f"Solution 2: {solution_2(input_2)}")


if __name__ == "__main__":
    main()

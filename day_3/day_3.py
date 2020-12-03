from math import prod
from multiprocessing import Pool
from typing import Iterator

from utils import read_input


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


def solution_2(slope, jumps):
    rounds = map(lambda x: (x[0], x[1], slope), jumps)
    results = map(lambda x: navigate(*x), rounds)
    return prod(results)


def solution_3(slope, p, jumps):
    rounds = map(lambda x: (x[0], x[1], slope), jumps)
    results = p.starmap(navigate, rounds)
    return prod(results)


def main():
    input_1 = read_input("./input_1.txt")
    print(f"Solution 1: {solution_1(input_1)}")
    input_2 = read_input("./input_2.txt")
    jumps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(f"Solution 2: {solution_2(input_2, jumps)}")
    with Pool(5) as p:
        print(f"Solution 3: {solution_3(input_2, p, jumps)}")


if __name__ == "__main__":
    main()

from typing import Iterator

from models import Password
from utils import read_input


def solution_1(passwords):
    return len(list(filter(lambda x: x.is_valid_1(), passwords)))


def solution_2(passwords):
    return len(list(filter(lambda x: x.is_valid_2(), passwords)))


def main():
    passwords: Iterator[Password] = read_input("./input_1.txt")
    print(f"Solution 1: {solution_1(passwords)}")
    passwords: Iterator[Password] = read_input("./input_2.txt")
    print(f"Solution 2: {solution_2(passwords)}")


if __name__ == "__main__":
    main()

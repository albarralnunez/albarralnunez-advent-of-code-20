from day_1 import solution as solution_1
from day1_v2 import solution as solution_2
from utils import read_input
import timeit


def test_1():
    entries = read_input("./input_3.txt")
    solution_1(entries, 3)


def test_2():
    entries = read_input("./input_3.txt")
    solution_2(entries, 3)


print("First Solution:")
print(timeit.timeit("test_1()", setup="from __main__ import test_1", number=100))
print("Second Solution:")
print(timeit.timeit("test_2()", setup="from __main__ import test_2", number=100))

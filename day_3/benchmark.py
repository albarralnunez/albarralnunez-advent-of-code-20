import time
from itertools import combinations
from multiprocessing import Pool

from day_3 import solution_2, solution_3
from utils import read_input

if __name__ == "__main__":
    runs = 1
    pool_size = 10
    jumps = list(combinations(range(1, 100), 2))
    small_slope = read_input("./input_2.txt")
    start_time_1 = time.time()
    for _ in range(runs):
        solution_2(small_slope, jumps)
    print(f"Solution 1 took {time.time() - start_time_1}")
    with Pool(pool_size) as p:
        start_time_2 = time.time()
        for _ in range(runs):
            solution_3(small_slope, p, jumps)
    print(f"Solution 2 took {time.time() - start_time_2}")
    big_slope = read_input("./input_3.txt")
    start_time_3 = time.time()
    for _ in range(runs):
        solution_2(big_slope, jumps)
    print(f"Solution 3 took {time.time() - start_time_3}")
    with Pool(pool_size) as p:
        start_time_4 = time.time()
        for _ in range(runs):
            solution_3(big_slope, p, jumps)
    print(f"Solution 4 took {time.time() - start_time_4}")

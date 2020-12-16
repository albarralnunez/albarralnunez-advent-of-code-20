
from operator import add, sub, mul
from functools import reduce
from itertools import zip_longest, chain


def div(x, y):
    if y == 0:
        return None
    return x/y

operations = [add, sub, mul, div]



def generate_opreations(posibilities: list, number: int) -> list[int]:
        combinations_operations = list(zip_longest([], posibilities, fillvalue=number))
        all_posible_operations = zip_longest([], operations, fillvalue=combinations_operations)
        all_results = list(filter(lambda x: x is not None, chain(
            *map(
                lambda x: map(
                    lambda y: x[1](y[0],y[1]),
                    x[0]
                ),
                all_posible_operations
            )
        )))
        return [min(all_results), max(all_results)]

def main(a, array):
    solution = list(reduce(generate_opreations, array, [a]))
    print(list(solution))
    return max(solution)

if __name__ == "__main__":
    first, *others = [1,0,12,-3]
    main(first, others)
import pytest

from main import (Problem1ApplyRules, Problem1SourrandingSeatsFinder,
                  Problem2ApplyRules, Problem2SourrandingSeatsFinder,
                  SeatLayout, read_input, solver)

finder_1 = Problem1SourrandingSeatsFinder()
rules_1 = Problem1ApplyRules()
finder_2 = Problem2SourrandingSeatsFinder()
rules_2 = Problem2ApplyRules()


test_inputs = [
    (read_input("./input_test_1_1.txt"), finder_1, rules_1, 37),
    (read_input("./input_test_1_2.txt"), finder_1, rules_1, 11),
    (read_input("./input_test_2_1.txt"), finder_2, rules_2, 5),
    (read_input("./input_test_2_2.txt"), finder_2, rules_2, 9),
    (read_input("./input_test_1_1.txt"), finder_2, rules_2, 26),
]


@pytest.mark.parametrize("test_input,finder,rules,expected", test_inputs)
def test(test_input, finder, rules, expected):
    seat_layout = SeatLayout.load(finder=finder, rules=rules, input_str=test_input)
    assert solver(seat_layout) == expected

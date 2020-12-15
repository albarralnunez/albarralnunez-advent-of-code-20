import pytest

from main import SeatLayout, problem_1, read_input

test_inputs = [
    (read_input("./input_test_1_1.txt"), 37),
    (read_input("./input_test_1_2.txt"), 11),
]

@pytest.mark.parametrize("test_input,expected", test_inputs)
def test_1(test_input, expected):
    seat_layout = SeatLayout.load(test_input)
    assert problem_1(seat_layout) == expected


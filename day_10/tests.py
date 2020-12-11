import pytest

from main import problem_1, problem_2, read_input

input_1 = read_input("./input_test_1.txt")
input_2 = read_input("./input_test_2.txt")

testdata_1 = [(input_1, 7 * 5), (input_2, 22 * 10)]
testdata_2 = [(input_1, 8), (input_2, 19208)]


@pytest.mark.parametrize("test_input,expected", testdata_1)
def test_1(test_input, expected):
    assert problem_1(test_input) == expected


@pytest.mark.parametrize("test_input,expected", testdata_2)
def test_2(test_input, expected):
    assert problem_2(test_input) == expected

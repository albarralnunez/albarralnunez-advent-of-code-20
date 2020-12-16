import pytest
from main import main


@pytest.mark.parametrize(
    "array,expected",
    [([1,0,12,-3], 36),
    ([1,12,3], 39)]
)
def tests(array, expected):
    first, *others = array
    assert main(first, others) == expected

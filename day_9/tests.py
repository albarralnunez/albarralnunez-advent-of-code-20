import pytest

from day_9 import problem_2


@pytest.mark.parametrize(
    "test_input, target, expected",
    [
        (
            [
                35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576,
            ],
            127,
            62,
        )
    ],
)
def test_problem_2(test_input, target, expected):
    assert expected == problem_2(test_input, target)

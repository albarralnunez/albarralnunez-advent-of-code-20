from day_3 import navigate


class TestSolution2:
    def test_1(self):
        slope = [
            "#..#..",
            "#..#..",
            "#..#..",
        ]
        result = navigate(3, 1, slope)
        assert result == 3

    def test_2(self):
        slope = [
            "#.",
            "#.",
            "#.",
        ]
        result = navigate(1, 1, slope)
        assert result == 2

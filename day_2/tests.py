from models import Password


class TestSolution1:
    def test_is_valid(self):
        password = Password(min=2, max=2, letter="a", value="aa")
        assert password.is_valid_1()

    def test_not_valid_min(self):
        password = Password(min=2, max=2, letter="a", value="a")
        assert not password.is_valid_1()

    def test_not_valid_max(self):
        password = Password(min=2, max=2, letter="a", value="aaa")
        assert not password.is_valid_1()


class TestSolution2:
    def test_is_valid(self):
        password = Password(min=1, max=2, letter="a", value="ac")
        assert password.is_valid_2()

    def test_not_valid_both(self):
        password = Password(min=1, max=2, letter="a", value="aa")
        assert not password.is_valid_2()

    def test_not_valid_none(self):
        password = Password(min=1, max=2, letter="a", value="bb")
        assert not password.is_valid_2()

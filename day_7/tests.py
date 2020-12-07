from day_7 import BagRule, Bags, read_rules


def test_1():
    bags = Bags(
        {
            "a": [BagRule(name="b", number=1)],
            "b": [BagRule(name="c", number=1), BagRule(name="e", number=1)],
            "c": [BagRule(name="d", number=1)],
            "d": [],
            "e": [BagRule(name="c", number=1)],
        }
    )
    assert bags.solution_1("c") == 3


def test_2():
    bags = Bags(
        {
            "a": [BagRule(name="b", number=2)],
            "b": [BagRule(name="c", number=2)],
            "c": [],
        }
    )
    assert bags.solution_2("a") == 6


def test_3():
    bags = Bags(
        {
            "a": [BagRule(name="b", number=1)],
            "b": [BagRule(name="c", number=1), BagRule(name="e", number=2)],
            "c": [BagRule(name="d", number=1)],
            "d": [],
            "e": [BagRule(name="d", number=1)],
        }
    )
    assert bags.solution_2("a") == 7


def test_4():
    bags_leadger = read_rules("./test_input_1.txt")
    bags = Bags()
    bags.create(bags_leadger)
    assert bags.solution_2("shiny gold") == 126


def test_5():
    bags_leadger = read_rules("./test_input_2.txt")
    bags = Bags()
    bags.create(bags_leadger)
    assert bags.solution_2("shiny gold") == 32

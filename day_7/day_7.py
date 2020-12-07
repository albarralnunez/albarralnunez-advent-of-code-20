import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, List

rule_re = r"^(.*)\sbags\scontain\s(.*[,.])+"
bags_re = r"(\d)\s([\w\s]*\s)bags?[,.]"


@dataclass
class BagRule:
    name: str
    number: int


class Bags:
    def __init__(self, bags=None):
        self._bags = bags or {}

    @classmethod
    def _create_bag(self, match: re.Match):
        number = int(match.group(1))
        name = match.group(2).strip()
        return BagRule(name=name, number=number)

    @classmethod
    def _parse_inner_bags(self, inner_bags: str) -> Iterator[BagRule]:
        bag_matches = re.finditer(bags_re, inner_bags)
        bag_rules = map(self._create_bag, bag_matches)
        return bag_rules

    def _add_bag(self, name: str, contains_definition: str):
        contains: Iterator[BagRule] = self._parse_inner_bags(contains_definition)
        self._bags[name] = list(contains)

    def create(self, rules_leadger: str):
        leadger_list = re.findall(rule_re, rules_leadger, re.MULTILINE)
        for name, contains in leadger_list:
            self._add_bag(name, contains)

    def can_hold(self, target_name: str, in_name: str):
        in_name_bags = list(map(lambda x: x.name, self._bags[in_name]))
        if target_name in in_name_bags:
            return True
        return any(
            map(lambda x: self.can_hold(target_name, x.name), self._bags[in_name])
        )

    def solution_1(self, target_name):
        bags_can_hold = map(lambda x: self.can_hold(target_name, x), self._bags.keys())
        return len(list(filter(None, bags_can_hold)))

    def _count(self, name: str, number: int):
        rules = self._bags[name]
        if not rules:
            return number
        number_of_bags = number + sum(
            map(lambda x: self._count(x.name, x.number * number), rules)
        )
        return number_of_bags

    def solution_2(self, name: str):
        return self._count(name, 1) - 1


def read_rules(input_file_path: str) -> str:
    with Path(input_file_path).open() as input:
        return input.read()


def main():
    rules_leadger_1 = read_rules("./input_1.txt")
    bags_1 = Bags()
    bags_1.create(rules_leadger_1)
    print(f"Solution 1: {bags_1.solution_1('shiny gold')}")
    rules_leadger_2 = read_rules("./input_2.txt")
    bags_2 = Bags()
    bags_2.create(rules_leadger_2)
    print(f"Solution 2: {bags_2.solution_2('shiny gold')}")


if __name__ == "__main__":
    main()

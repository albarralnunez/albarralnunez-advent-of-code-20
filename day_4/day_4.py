import re

from models import PassportValidator
from utils import read_input, read_input_text


def is_passport_valid(passport):
    required = [
        "byr", "iyr", "eyr", "hgt",
        "hcl", "ecl", "pid",
    ]
    return all(map(lambda x: x in passport, required))


def solution(passports, validator):
    return len(list(filter(None, map(validator, passports))))

def solution_one_regex(passports):
        regex =(
            r"("
            r"(?=.*byr:(?P<byr>(?:(?:19[2-9][0-9])|(?:200[0-2])))(?:\s|$))"
            r"(?=.*iyr:(?P<iyr>2(?:01[0-9]|020))(?:\s|$))"
            r"(?=.*eyr:(?P<eyr>2(?:02[0-9]|030))(?:\s|$))"
            r"(?=.*hgt:(?P<hgt>(1(?:[5-9][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in))(?:\s|$))"
            r"(?=.*hcl:(?P<hcl>\#[0-9a-f]{6})(?:\s|$))"
            r"(?=.*ecl:(?P<ecl>(?:amb|blu|brn|gry|grn|hzl|oth))(?:\s|$))"
            r"(?=.*pid:(?P<pid>\d{9})(?:\s|$))"
            r")+"
        )
        return len(list(re.finditer(regex, passports)))

def main():
    passports_1 = read_input("./input_1.txt")
    print(f"Solution 1: {solution(passports_1, is_passport_valid)}")
    passports_2 = read_input("./input_2.txt")
    passport_validator = PassportValidator()
    print(f"Solution 2: {solution(passports_2, passport_validator)}")
    passports_2 = read_input_text("./input_2.txt")
    print(f"Solution 3: {solution_one_regex(passports_2)}")



if __name__ == "__main__":
    main()

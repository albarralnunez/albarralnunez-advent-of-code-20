import re

from models import PassportValidator
from utils import read_input


def is_passport_valid(passport):
    required = [
        "byr", "iyr", "eyr", "hgt",
        "hcl", "ecl", "pid",
    ]
    return all(map(lambda x: x in passport, required))


def solution(passports, validator):
    return len(list(filter(None, map(validator, passports))))


def main():
    passports_1 = read_input("./input_1.txt")
    print(f"Solution 1: {solution(passports_1, is_passport_valid)}")
    passports_2 = read_input("./input_2.txt")
    passport_validator = PassportValidator()
    print(f"Solution 2: {solution(passports_2, passport_validator)}")


if __name__ == "__main__":
    main()

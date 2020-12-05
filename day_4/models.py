import re
from dataclasses import dataclass


@dataclass
class PassportValidator:

    PASSPORT_RE = re.compile(
        r"(?=.*byr:(?P<byr>(?:(?:19[2-9][0-9])|(?:200[0-2])))(?:\s|$))"
        r"(?=.*iyr:(?P<iyr>2(?:01[0-9]|020))(?:\s|$))"
        r"(?=.*eyr:(?P<eyr>2(?:02[0-9]|030))(?:\s|$))"
        r"(?=.*hgt:(?P<hgt>(1(?:[5-9][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in))(?:\s|$))"
        r"(?=.*hcl:(?P<hcl>\#[0-9a-f]{6})(?:\s|$))"
        r"(?=.*ecl:(?P<ecl>(?:amb|blu|brn|gry|grn|hzl|oth))(?:\s|$))"
        r"(?=.*pid:(?P<pid>\d{9})(?:\s|$))"
    )

    def __call__(self, passport: str):
        normalized_passport = passport.replace("\n", " ")
        passport_match = self.PASSPORT_RE.match(normalized_passport)
        return bool(passport_match)

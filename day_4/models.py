import re
from dataclasses import dataclass


@dataclass
class PassportValidator:

    PASSPORT_RE = re.compile(
        r"(?=.*byr:(?P<byr>\d{4})(?:\s|$))"
        r"(?=.*iyr:(?P<iyr>\d{4})(?:\s|$))"
        r"(?=.*eyr:(?P<eyr>\d{4})(?:\s|$))"
        r"(?=.*hgt:(?P<hgt>\d+(?:cm|in))(?:\s|$))"
        r"(?=.*hcl:(?P<hcl>\#[0-9a-f]{6})(?:\s|$))"
        r"(?=.*ecl:(?P<ecl>(?:amb|blu|brn|gry|grn|hzl|oth))(?:\s|$))"
        r"(?=.*pid:(?P<pid>\d{9})(?:\s|$))"
    )

    def __call__(self, passport: str):
        normalized_passport = passport.replace("\n", " ")
        passport_match = self.PASSPORT_RE.match(normalized_passport)
        if not passport_match:
            return False
        byr = int(passport_match.group("byr"))
        iyr = int(passport_match.group("iyr"))
        eyr = int(passport_match.group("eyr"))
        hgt = passport_match.group("hgt")
        hgt_value, hgt_unit = int(hgt[:-2]), hgt[-2:]
        byr_corr = 1920 <= byr <= 2020
        iyr_corr = 2010 <= iyr <= 2020
        eyr_corr = 2020 <= eyr <= 2030
        hgt_cm_corr = 150 <= hgt_value <= 193 and hgt_unit == "cm"
        hgt_in_corr = 59 <= hgt_value <= 76 and hgt_unit == "in"
        hgt_corr = hgt_cm_corr or hgt_in_corr
        integrity_restrictions = byr_corr and iyr_corr and eyr_corr and hgt_corr
        return integrity_restrictions

from dataclasses import dataclass


@dataclass(frozen=True)
class Password:
    min: int
    max: int
    letter: str
    value: str

    def __str__(self):
        return f"{self.min}-{self.max} {self.letter}: {self.value}"

    def _match_letter(self, letter):
        return letter == self.letter

    def is_valid_1(self):
        number_of_letters = len(list(filter(self._match_letter, self.value)))
        return self.min <= number_of_letters and self.max >= number_of_letters

    def is_valid_2(self):
        number_of_letters = len(
            list(
                filter(
                    self._match_letter,
                    self.value[self.min - 1] + self.value[self.max - 1],
                )
            )
        )
        return number_of_letters == 1

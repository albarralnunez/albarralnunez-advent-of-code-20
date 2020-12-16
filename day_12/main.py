from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import re
from typing import Iterable, Literal, Tuple, ClassVar, Pattern, Union, get_args, Type

CardinalPoint = Literal["N", "W", "S", "E"]
Rotation = Literal["R", "L"]
MoveForward = Literal["F"]
Action = Union[MoveForward, CardinalPoint, Rotation]
Position = Tuple[int, int]
Movement = Tuple[Action, int]
Leadger = Iterable[Movement]


@dataclass
class Boat:
    position: Position = field(default_factory=lambda: (0, 0))

    @property
    def solution(self):
        return abs(self.position[0]) + abs(self.position[1])


@dataclass
class Problem1Boat(Boat):
    _orientation: int = field(init=False, repr=False, default=90)

    @property
    def orientation(self) -> int:
        return self._orientation % 360

    def _rotate(self, action: Rotation, value: int):
        if action == "R":
            self._orientation += value
        elif action == "L":
            self._orientation -= value

    def _move_forward(self, value):
        if self.orientation == 0:
            self.position = (self.position[0], self.position[1] + value)
        if self.orientation == 90:
            self.position = (self.position[0] + value, self.position[1])
        if self.orientation == 180:
            self.position = (self.position[0], self.position[1] - value)
        if self.orientation == 270:
            self.position = (self.position[0] - value, self.position[1])

    def _move_direction(self, action: CardinalPoint, value: int):
        if action == "N":
            self.position = (self.position[0], self.position[1] + value)
        elif action == "E":
            self.position = (self.position[0] + value, self.position[1])
        elif action == "S":
            self.position = (self.position[0], self.position[1] - value)
        elif action == "W":
            self.position = (self.position[0] - value, self.position[1])

    def move(self, action: Action, value: int):
        if action in get_args(CardinalPoint):
            self._move_direction(action, value)
        elif action in get_args(Rotation):
            self._rotate(action, value)
        elif action in get_args(MoveForward):
            self._move_forward(value)

"""
@@@@@@
@X@@@@
@@X@@@
@@@X@@
@@@@@@
"""

@dataclass
class Problem2Boat(Boat):
    _way_point_position: Position = field(default_factory=lambda: (10, 1))

    def _rotate_way_point(self, action: Rotation, value: int):
        if (
            value == 90 and action == "R"
            or value == 270 and action == "L"
        ):
            self.position = (
                self.position[1] * (self.position[0]/abs(self.position[0])),
                self.position[0] * (self.position[1]/abs(self.position[1])),
            )

    def _move_forward(self, value):
        self.position = (
            self.position[0] + self._way_point_position[0] * value,
            self.position[1] + self._way_point_position[1] * value,
        )

    def _move_way_point(self, action: CardinalPoint, value: int):
        if action == "N":
            self._way_point_position = (
                self._way_point_position[0],
                self._way_point_position[1] + value,
            )
        elif action == "E":
            self._way_point_position = (
                self._way_point_position[0] + value,
                self._way_point_position[1],
            )
        elif action == "S":
            self._way_point_position = (
                self._way_point_position[0],
                self._way_point_position[1] - value,
            )
        elif action == "W":
            self._way_point_position = (
                self._way_point_position[0] - value,
                self._way_point_position[1],
            )

    def move(self, action: Action, value: int):
        if action in get_args(CardinalPoint):
            self._move_way_point(action, value)
        elif action in get_args(Rotation):
            self._rotate_way_point(action, value)
        elif action in get_args(MoveForward):
            self._move_forward(value)


@dataclass
class LeadgerReader:

    leadger_re: ClassVar[Pattern] = re.compile(r"([NSEWLRF])(\d+)")

    def _read_file(self, path: Path):
        with Path(path).open() as f:
            leadger_text = f.read()
            return leadger_text

    def __call__(self, path: str) -> Leadger:
        leadger_text: str = self._read_file(Path(path))
        leadger: Leadger = self.leadger_re.findall(leadger_text)
        return leadger


def solver(problme_boat_type: Type[Boat], leadger: Leadger):
    boat = problme_boat_type()
    for action, value in leadger:
        boat.move(action, int(value))
    return boat.solution


def main():
    leadger_reader = LeadgerReader()
    leadger_test = leadger_reader("./test_input.txt")
    leadger = leadger_reader("./input.txt")
    solution_test_1 = solver(Problem1Boat, leadger_test)
    print(f"Solution Test 1: {solution_test_1}")
    solution_problem_1 = solver(Problem1Boat, leadger)
    print(f"Solution Problem 1: {solution_problem_1}")
    solution_test_2 = solver(Problem2Boat, leadger_test)
    print(f"Solution Test 2: {solution_test_2}")
    solution_problem_2 = solver(Problem2Boat, leadger)
    print(f"Solution Problem 2: {solution_problem_2}")


if __name__ == "__main__":
    main()

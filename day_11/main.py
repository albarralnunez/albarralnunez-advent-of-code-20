from copy import deepcopy
from dataclasses import dataclass, field
# import only system from os
from os import name, system
from pathlib import Path
# import sleep to show output for some time period
from time import sleep
from typing import List, Literal, Optional

SeatState = Literal["L", "#", "."]

flatten = lambda t: [item for sublist in t for item in sublist]


def clear():
    """
    Define our clear function
    """
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


@dataclass(frozen=True)
class Seat:
    x: int
    y: int
    state: SeatState

    def __str__(self):
        return self.state

    def __eq__(self, x):
        if isinstance(x, str):
            return self.state == x
        return self.state == x.state


@dataclass(frozen=True)
class SeatLayout:
    layout: List[List[Seat]]

    @property
    def x_len(self):
        return len(self.layout[0])

    @property
    def y_len(self):
        return len(self.layout)

    @classmethod
    def load(cls, input_str: str) -> "SeatLayout":
        layout = list(
            map(
                lambda y: list(
                    map(
                        lambda x: Seat(x=x[0], y=y[0], state=y[1][x[0]]),  # type: ignore
                        enumerate(y[1]),
                    )
                ),
                enumerate(input_str.split()),
            )
        )
        return SeatLayout(layout)

    def _get_sourranding_seats(self, seat) -> List[Seat]:
        x_left = 0
        x_right = 0
        y_down = 1
        y_up = -1
        up_seats = []
        down_seats = []
        left_seat = None
        right_seat = None
        if seat.x > 0:
            x_left = -1
            left_seat = self.layout[seat.y][seat.x + x_left]
        if seat.x + x_right < self.x_len - 1:
            x_right = 1
            right_seat = self.layout[seat.y][seat.x + x_right]
        if seat.y + y_up > 0:
            up_seats = self.layout[seat.y + y_up][
                seat.x + x_left : seat.x + x_right + 1
            ]
        if seat.y < self.y_len - 1:
            down_seats = self.layout[seat.y + y_down][
                seat.x + x_left : seat.x + x_right + 1
            ]
        surrounding_seats: List[Seat] = list(
            filter(None, (left_seat, *up_seats, *down_seats, right_seat))
        )
        return surrounding_seats

    def _apply_rule(self, seat) -> Seat:
        surrounding_seats = self._get_sourranding_seats(seat)
        if seat == "L":
            if all(map(lambda x: x == "L" or x == ".", surrounding_seats)):
                return Seat(seat.x, seat.y, "#")
        elif seat == "#":
            if 4 <= surrounding_seats.count("#"):  # type: ignore
                return Seat(seat.x, seat.y, "L")
        return seat

    def step(self) -> "SeatLayout":
        return SeatLayout(
            list(map(lambda x: list(map(self._apply_rule, x)), self.layout))
        )

    def count_occupaied(self):
        return flatten(self.layout).count("#")  # type: ignore

    def __str__(self):
        return "\n".join(map(lambda x: "".join(map(str, x)), self.layout))

    def __eq__(self, other):
        zip_matrix = list(
            flatten(
                map(
                    lambda x: list(zip(x[0], x[1])),
                    list(zip(self.layout, other.layout)),
                )
            )
        )
        flatten_matrix = map(lambda x: x[0] == x[1], zip_matrix)
        return all(flatten_matrix)

def print_layout(seat_layout: SeatLayout):
    clear()
    print("O"*seat_layout.x_len)
    print(seat_layout)
    sleep(0.5)

def problem_1(seat_layout: SeatLayout, show_layout: bool = False):
    old_layout = seat_layout
    if show_layout:
        print_layout(old_layout)
    next_layout = seat_layout.step()
    while old_layout != next_layout:
        old_layout = next_layout
        if show_layout:
            print_layout(old_layout)
        next_layout = next_layout.step()
    return next_layout.count_occupaied()


def read_input(path: str):
    with Path(path).open() as f:
        return f.read()


def main():
    seat_layout_input_test_1_1 = read_input("./input_test_1_1.txt")
    seat_layout_test_1_1 = SeatLayout.load(seat_layout_input_test_1_1)
    print(f"Solution Test 1 v1: {problem_1(seat_layout_test_1_1, True)}")
    print("H"*seat_layout_test_1_1.x_len)
    seat_layout_input_test_1_2 = read_input("./input_test_1_2.txt")
    seat_layout_test_1_2 = SeatLayout.load(seat_layout_input_test_1_2)
    print(f"Solution Test 1 v2: {problem_1(seat_layout_test_1_2, True)}")
    print("H"*seat_layout_test_1_2.x_len)
    seat_layout_input = read_input("./input.txt")
    seat_layout = SeatLayout.load(seat_layout_input)
    print(f"Solution Problem 1: {problem_1(seat_layout, True)}")


if __name__ == "__main__":
    main()

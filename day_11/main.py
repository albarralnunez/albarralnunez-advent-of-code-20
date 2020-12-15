import argparse
from copy import deepcopy
from dataclasses import dataclass, field
from os import name, system
from pathlib import Path
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

    @property
    def is_valid_seat(self) -> bool:
        return self.state == "#" or self.state == "L"

    @property
    def is_empty(self) -> bool:
        return self.state == "." or self.state == "L"

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.state == other
        return self.state == other.state


class SourrandingSeatsFinder:
    def __call__(self, layout: "SeatLayout", seat: Seat) -> List[Seat]:
        raise NotImplementedError


class Problem1SourrandingSeatsFinder(SourrandingSeatsFinder):
    def __call__(self, layout: "SeatLayout", seat: Seat) -> List[Seat]:
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
            left_seat = layout.layout[seat.y][seat.x + x_left]
        if seat.x + x_right < layout.x_len - 1:
            x_right = 1
            right_seat = layout.layout[seat.y][seat.x + x_right]
        if seat.y > 0:
            up_seats = layout.layout[seat.y + y_up][
                seat.x + x_left : seat.x + x_right + 1
            ]
        if seat.y < layout.y_len - 1:
            down_seats = layout.layout[seat.y + y_down][
                seat.x + x_left : seat.x + x_right + 1
            ]
        surrounding_seats: List[Seat] = list(
            filter(None, (left_seat, *up_seats, *down_seats, right_seat))
        )
        return surrounding_seats


class Problem2SourrandingSeatsFinder(SourrandingSeatsFinder):
    def out_of_matrix(self, position_x, position_y, len_x, len_y):
        return (
            position_y < 0
            or position_x < 0
            or position_x > len_x - 1
            or position_y > len_y - 1
        )

    def find_seat(
        self, layout: "SeatLayout", seat: Seat, direction_x, direction_y
    ) -> Optional[Seat]:
        position_y = seat.y + direction_y
        position_x = seat.x + direction_x
        # print(f"?({direction_x}, {direction_y})") # TODO: DELETE
        if self.out_of_matrix(position_x, position_y, layout.x_len, layout.y_len):
            return None
        result = layout.get(position_x, position_y)
        # print(f"*({position_x}, {position_y}): {result.is_valid_seat}, {result}") # TODO: DELETE
        # if seat.x == 3 and seat.y == 4: print(layout) # TODO: DELETE
        while not result.is_valid_seat:
            position_x += direction_x
            position_y += direction_y
            if self.out_of_matrix(position_x, position_y, layout.x_len, layout.y_len):
                return None
            result = layout.get(position_x, position_y)
            # print(f"*({position_x}, {position_y}): {result.is_valid_seat}, {result}") # TODO: DELETE
            # if seat.x == 3 and seat.y == 4: print(layout) # TODO: DELETE
        # print(f"->({result.x}, {result.y})") # TODO: DELETE
        return result

    def __call__(self, layout: "SeatLayout", seat: Seat) -> List[Seat]:
        return list(
            filter(
                None,
                [
                    self.find_seat(layout, seat, 0, 1),
                    self.find_seat(layout, seat, 1, 0),
                    self.find_seat(layout, seat, 0, -1),
                    self.find_seat(layout, seat, -1, 0),
                    self.find_seat(layout, seat, -1, 1),
                    self.find_seat(layout, seat, 1, -1),
                    self.find_seat(layout, seat, 1, 1),
                    self.find_seat(layout, seat, -1, -1),
                ],
            )
        )


class ApplyRules:
    def __call__(self, seat: Seat, surrounding_seats: List[Seat]) -> Seat:
        raise NotImplementedError


class Problem1ApplyRules:
    def __call__(self, seat: Seat, surrounding_seats: List[Seat]) -> Seat:
        if seat == "L":
            if all(map(lambda x: x.is_empty, surrounding_seats)):
                return Seat(seat.x, seat.y, "#")
        elif seat == "#":
            if 4 <= surrounding_seats.count("#"):  # type: ignore
                return Seat(seat.x, seat.y, "L")
        return seat


class Problem2ApplyRules:
    def __call__(self, seat: Seat, surrounding_seats: List[Seat]) -> Seat:
        if seat == "L":
            if all(map(lambda x: x.is_empty, surrounding_seats)):
                return Seat(seat.x, seat.y, "#")
        elif seat == "#":
            if 5 <= surrounding_seats.count("#"):  # type: ignore
                return Seat(seat.x, seat.y, "L")
        return seat


@dataclass(frozen=True)
class SeatLayout:
    layout: List[List[Seat]]
    finder: SourrandingSeatsFinder
    rules: ApplyRules

    @property
    def x_len(self):
        return len(self.layout[0])

    @property
    def y_len(self):
        return len(self.layout)

    @classmethod
    def load(
        cls, rules: ApplyRules, finder: SourrandingSeatsFinder, input_str: str
    ) -> "SeatLayout":
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
        return SeatLayout(layout, rules=rules, finder=finder)

    def get(self, x: int, y: int) -> Seat:
        return self.layout[y][x]

    def _apply_rule(self, seat) -> Seat:
        if seat == ".":
            return seat
        # print(f"{seat.x},{seat.y}") #TODO: DELETE
        surrounding_seats = self.finder(self, seat)
        # print(surrounding_seats) #TODO: DELETE
        seat = self.rules(seat, surrounding_seats)
        return seat

    def step(self) -> "SeatLayout":
        return SeatLayout(
            layout=list(map(lambda x: list(map(self._apply_rule, x)), self.layout)),
            finder=self.finder,
            rules=self.rules,
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
    print("O" * seat_layout.x_len)
    print(seat_layout)
    sleep(0.5)


def solver(seat_layout: SeatLayout, show_layout: bool = False):
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


def main(args):
    seat_layout_input = read_input("./input.txt")

    seat_layout_input_test_1_1 = read_input("./input_test_1_1.txt")
    seat_layout_input_test_1_2 = read_input("./input_test_1_2.txt")
    finder_problem_1 = Problem1SourrandingSeatsFinder()
    apply_rule_problem_1 = Problem1ApplyRules()

    # PROBLEM 1
    seat_layout_test_1_1 = SeatLayout.load(
        input_str=seat_layout_input_test_1_1,
        finder=finder_problem_1,
        rules=apply_rule_problem_1,
    )
    print(f"Solution Test 1 v1: {solver(seat_layout_test_1_1, args.print)}")
    if args.print:
        print("H" * seat_layout_test_1_1.x_len)

    seat_layout_test_1_2 = SeatLayout.load(
        input_str=seat_layout_input_test_1_2,
        finder=finder_problem_1,
        rules=apply_rule_problem_1,
    )
    print(f"Solution Test 1 v2: {solver(seat_layout_test_1_2, args.print)}")
    if args.print:
        print("H" * seat_layout_test_1_2.x_len)

    seat_layout_1 = SeatLayout.load(
        input_str=seat_layout_input, finder=finder_problem_1, rules=apply_rule_problem_1
    )
    print(f"Solution Problem 1: {solver(seat_layout_1, args.print)}")
    if args.print:
        print("H" * seat_layout_1.x_len)

    # PROBLEM 2
    seat_layout_input_test_2_1 = read_input("./input_test_2_1.txt")
    seat_layout_input_test_2_2 = read_input("./input_test_2_2.txt")
    finder_problem_2 = Problem2SourrandingSeatsFinder()
    apply_rule_problem_2 = Problem2ApplyRules()

    seat_layout_test_2_1 = SeatLayout.load(
        input_str=seat_layout_input_test_2_1,
        finder=finder_problem_2,
        rules=apply_rule_problem_2,
    )
    print(f"Solution Test 2 v1: {solver(seat_layout_test_2_1, args.print)}")
    if args.print:
        print("H" * seat_layout_test_2_1.x_len)

    seat_layout_test_2_2 = SeatLayout.load(
        input_str=seat_layout_input_test_2_2,
        finder=finder_problem_2,
        rules=apply_rule_problem_2,
    )
    print(f"Solution Test 2 v2: {solver(seat_layout_test_2_2, args.print)}")
    if args.print:
        print("H" * seat_layout_test_2_2.x_len)

    seat_layout_test_2_3 = SeatLayout.load(
        input_str=seat_layout_input_test_1_1,
        finder=finder_problem_2,
        rules=apply_rule_problem_2,
    )
    print(f"Solution Test 2 v3: {solver(seat_layout_test_2_3, args.print)}")
    if args.print:
        print("H" * seat_layout_test_2_2.x_len)

    seat_layout_2 = SeatLayout.load(
        input_str=seat_layout_input, finder=finder_problem_2, rules=apply_rule_problem_2
    )
    print(f"Solution Problem 2: {solver(seat_layout_2, args.print)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--print", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    main(args)

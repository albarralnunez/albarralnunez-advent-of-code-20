import pytest

from day_5 import get_coloumn, get_id, get_position, get_row


@pytest.mark.parametrize("ticket,ticket_coloumn", [("RRR", 7), ("LLL", 0), ("RLL", 4)])
def test_get_coloumn(ticket, ticket_coloumn):
    assert get_coloumn(ticket) == ticket_coloumn


@pytest.mark.parametrize(
    "ticket,ticket_row",
    [
        ("BFFFBBF", 70),
        ("FFFBBBF", 14),
        ("BBFFBBF", 102),
        ("FFFFFFF", 0),
        ("BBBBBBB", 127),
        ("BBBBBBF", 126),
    ],
)
def test_get_row(ticket, ticket_row):
    assert get_row(ticket) == ticket_row


@pytest.mark.parametrize(
    "ticket,ticket_possition",
    [("BFFFBBFRRR", (70, 7)), ("FFFBBBFRRR", (14, 7)), ("BBFFBBFRLL", (102, 4))],
)
def test_get_possition(ticket, ticket_possition):
    assert get_position(ticket) == ticket_possition

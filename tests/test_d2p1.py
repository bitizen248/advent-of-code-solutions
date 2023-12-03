import pytest

from day_2.part_1 import find_sum_possible_id
from day_2.part_1 import is_bag_possible
from day_2.part_1 import parse_blocks_line
from day_2.part_1 import parse_game_line


def test_blocks_parser():
    line = "12 red, 13 green, 14 blue"
    assert parse_blocks_line(line) == {"red": 12, "green": 13, "blue": 14}


def test_game_line_parser():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    res = parse_game_line(line)
    assert res == {
        "game_id": 1,
        "blocks": [
            {"blue": 3, "red": 4},
            {"red": 1, "green": 2, "blue": 6},
            {"green": 2},
        ],
    }


@pytest.mark.parametrize(
    "blocks,res",
    [
        (
            [
                {"blue": 3, "red": 4},
                {"red": 1, "green": 2, "blue": 6},
                {"green": 2},
            ],
            True,
        ),
        (
            [
                {"blue": 1, "green": 2},
                {"green": 3, "blue": 4, "red": 1},
                {"blue": 1, "green": 1},
            ],
            True,
        ),
        (
            [
                {"green": 8, "blue": 6, "red": 20},
                {"blue": 5, "red": 4, "green": 13},
                {"green": 5, "red": 1},
            ],
            False,
        ),
        (
            [
                {"green": 1, "red": 3, "blue": 6},
                {"green": 3, "red": 6},
                {"green": 3, "blue": 15, "red": 14},
            ],
            False,
        ),
        ([{"red": 6, "blue": 1, "green": 3}, {"blue": 2, "red": 1, "green": 2}], True),
    ],
)
def test_is_game_possible(blocks, res):
    bag = {"red": 12, "green": 13, "blue": 14}
    assert is_bag_possible(blocks, bag) == res


@pytest.fixture()
def lines():
    return [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]


def test_full_coverage(lines):
    assert find_sum_possible_id(lines, "12 red, 13 green, 14 blue") == 8

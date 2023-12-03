import pytest

from day_2.part_2 import get_game_power
from day_2.part_2 import sum_games_powers


@pytest.mark.parametrize(
    "blocks,res",
    [
        (
                [
                    {"blue": 3, "red": 4},
                    {"red": 1, "green": 2, "blue": 6},
                    {"green": 2}
                ],
                48
        ),
        (
                [
                    {"blue": 1, "green": 2},
                    {"green": 3, "blue": 4, "red": 1},
                    {"green": 1, "blue": 1}
                ],
                12
        ),
        (
                [
                    {"green": 8, "blue": 6, "red": 20},
                    {"blue": 5, "red": 4, "green": 13},
                    {"green": 5, "red": 1}
                ],
                1560
        ),
        (
                [
                    {"green": 1, "red": 3, "blue": 6},
                    {"green": 3, "red": 6},
                    {"green": 3, "blue": 15, "red": 14}
                ],
                630
        ),
        (
                [
                    {"red": 6, "blue": 1, "green": 3},
                    {"blue": 2, "red": 1, "green": 2}
                ], 36
        )
    ]
)
def test_game_power(blocks, res):
    assert get_game_power(blocks) == res


@pytest.fixture()
def lines():
    return [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]


def test_sum_games_powers(lines):
    assert sum_games_powers(lines) == 2286

import pytest

from day_3.part_2 import multiply_all_gears


@pytest.fixture()
def matrix():
    data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.",
    ]
    return [[c for c in line] for line in data]


def test_multiply_all_gears(matrix):
    assert multiply_all_gears(matrix) == 467835

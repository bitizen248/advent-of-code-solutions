import pytest

from day_3.common import cut_number
from day_3.part_1 import sum_numbers_near_symbols


@pytest.mark.parametrize(
    "matrix,cut,res",
    [
        (
            [
                [".", ".", ".", ".", "."],
                [".", "3", "2", "1", "."],
                [".", ".", ".", ".", "."],
            ],
            (1, 2),
            321,
        ),
        (
            [
                ["3", "4", "5", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
            ],
            (0, 0),
            345,
        ),
    ],
)
def test_cut_number(matrix, cut, res):
    assert cut_number(matrix, cut) == res


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


def test_sum_numbers_near_symbols(matrix):
    assert sum_numbers_near_symbols(matrix) == 4361

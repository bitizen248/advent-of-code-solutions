import pytest

from day_4.common import parse_card
from day_4.part_1 import calculate_total_cards_value
from day_4.part_1 import value_card


@pytest.mark.parametrize(
    "line,res",
    [
        (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            {
                "winning_numbers": [41, 48, 83, 86, 17],
                "card_numbers": [83, 86, 6, 31, 17, 9, 48, 53],
            },
        ),
        (
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            {
                "winning_numbers": [13, 32, 20, 16, 61],
                "card_numbers": [61, 30, 68, 82, 17, 32, 24, 19],
            },
        ),
        (
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            {
                "winning_numbers": [1, 21, 53, 59, 44],
                "card_numbers": [69, 82, 63, 72, 16, 21, 14, 1],
            },
        ),
        (
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            {
                "winning_numbers": [41, 92, 73, 84, 69],
                "card_numbers": [59, 84, 76, 51, 58, 5, 54, 83],
            },
        ),
        (
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            {
                "winning_numbers": [87, 83, 26, 28, 32],
                "card_numbers": [88, 30, 70, 12, 93, 22, 82, 36],
            },
        ),
        (
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
            {
                "winning_numbers": [31, 18, 13, 56, 72],
                "card_numbers": [74, 77, 10, 23, 35, 67, 36, 11],
            },
        ),
    ],
)
def test_parse_card(line, res):
    assert parse_card(line) == res


@pytest.mark.parametrize(
    "card,value",
    [
        (
            {
                "winning_numbers": [41, 48, 83, 86, 17],
                "card_numbers": [83, 86, 6, 31, 17, 9, 48, 53],
            },
            8,
        ),
        (
            {
                "winning_numbers": [13, 32, 20, 16, 61],
                "card_numbers": [61, 30, 68, 82, 17, 32, 24, 19],
            },
            2,
        ),
        (
            {
                "winning_numbers": [1, 21, 53, 59, 44],
                "card_numbers": [69, 82, 63, 72, 16, 21, 14, 1],
            },
            2,
        ),
        (
            {
                "winning_numbers": [41, 92, 73, 84, 69],
                "card_numbers": [59, 84, 76, 51, 58, 5, 54, 83],
            },
            1,
        ),
        (
            {
                "winning_numbers": [87, 83, 26, 28, 32],
                "card_numbers": [88, 30, 70, 12, 93, 22, 82, 36],
            },
            0,
        ),
        (
            {
                "winning_numbers": [31, 18, 13, 56, 72],
                "card_numbers": [74, 77, 10, 23, 35, 67, 36, 11],
            },
            0,
        ),
    ],
)
def test_card_valuation(card, value):
    assert value_card(card) == value


@pytest.fixture()
def lines():
    return [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]


def test_calculate_total_cards_value(lines):
    assert calculate_total_cards_value(lines) == 13

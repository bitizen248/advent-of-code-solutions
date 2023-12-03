import pytest

from day_1.part_2 import get_calibration_number
from day_1.part_2 import get_number_from_line


@pytest.mark.parametrize(
    "line,res",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_get_number_form_line(line, res):
    assert get_number_from_line(line) == res


@pytest.fixture()
def lines():
    return [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]


def test_full_coverage(lines):
    assert get_calibration_number(lines) == 281

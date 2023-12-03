import pytest

from day_1.part_1 import get_calibration_number
from day_1.part_1 import get_number_from_line


@pytest.mark.parametrize(
    "line,res",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_algroithm(line, res):
    assert get_number_from_line(line) == res

@pytest.fixture()
def lines():
    return [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

def test_full_coverage(lines):
    assert get_calibration_number(lines) == 142

from day_4.common import parse_card


def value_card(card):
    winning_numbers = set(card["winning_numbers"])
    card_numbers = set(card["card_numbers"])

    common = winning_numbers.intersection(card_numbers)

    if not common:
        return 0
    res = 1
    for _ in range(len(common) - 1):
        res *= 2
    return res


def calculate_total_cards_value(lines):
    res = 0
    for line in lines:
        card = parse_card(line)
        res += value_card(card)
    return res


if __name__ == "__main__":
    data = open("input/day_4.txt")
    print(calculate_total_cards_value(data))
    data.close()

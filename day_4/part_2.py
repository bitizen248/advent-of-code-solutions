from day_4.common import parse_card


def value_card(card):
    winning_numbers = set(card["winning_numbers"])
    card_numbers = set(card["card_numbers"])

    common = winning_numbers.intersection(card_numbers)

    return len(common)


def calculate_total_cards_value(lines):
    card_multi = {1: 1}
    i = 1
    for line in lines:
        card = parse_card(line)
        win = value_card(card)
        if i not in card_multi:
            card_multi[i] = 1
        for j in range(win):
            if i + j + 1 not in card_multi:
                card_multi[i + j + 1] = 1
            card_multi[i + j + 1] += card_multi[i]
        i += 1
    return sum(card_multi.values())


if __name__ == "__main__":
    data = open("input/day_4.txt")
    print(calculate_total_cards_value(data))
    data.close()

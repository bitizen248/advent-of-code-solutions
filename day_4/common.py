def parse_card(card_line):
    _, numbers = card_line.split(":")
    winning_numbers, card_numbers = numbers.split("|")
    winning_numbers = [int(n) for n in winning_numbers.split()]
    card_numbers = [int(n) for n in card_numbers.split()]

    return {"winning_numbers": winning_numbers, "card_numbers": card_numbers}

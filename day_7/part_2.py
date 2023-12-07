from functools import cmp_to_key

from day_7.test import expected

cards_value = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


def value_hand(hand):
    count = dict()
    for v in hand:
        if v not in count:
            count[v] = 1
        else:
            count[v] += 1
    wildcards = count.get("J", 0)
    if wildcards == 5:
        return 7
    if wildcards:
        del count["J"]
        max_keys = sorted(count.items(), key=lambda v: v[1], reverse=True)[0][0]
        count[max_keys] += wildcards
    if len(count) == 1:
        return 7
    if len(count) == 2:
        if set(count.values()) == {1, 4}:
            return 6
        return 5
    if len(count) == 3:
        if set(count.values()) == {3, 1, 1}:
            return 4
        if set(count.values()) == {2, 2, 1}:
            return 3
    if len(count) == 4:
        return 2
    return 1


def compare_hands(hand_1, hand_2):
    hand_1, _ = hand_1
    hand_2, _ = hand_2
    value_1 = value_hand(hand_1)
    value_2 = value_hand(hand_2)
    if value_1 == value_2:
        if hand_1 == hand_2:
            return 0
        i = 0
        while hand_1[i] == hand_2[i]:
            i += 1
        return 1 if cards_value[hand_1[i]] > cards_value[hand_2[i]] else -1
    return 1 if value_1 > value_2 else -1


def calculate_win(lines):
    hands = list()
    for line in lines:
        hand, bid = line.split()
        hands.append((hand, int(bid)))
    hands = sorted(hands, key=cmp_to_key(compare_hands))

    for i in range(len(hands)):
        if expected[i] != hands[i][0]:
            break
    res = 0
    i = 1
    for _, bid in hands:
        res += bid * i
        i += 1
    return res


if __name__ == "__main__":
    data = open("input/day_7.txt")
    print(calculate_win(data))
    data.close()

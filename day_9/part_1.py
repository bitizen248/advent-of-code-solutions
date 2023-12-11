def find_dif_list(numbers_list):
    diff = list()
    for i in range(1, len(numbers_list)):
        diff.append(numbers_list[i] - numbers_list[i - 1])
    return diff


def predict_number(numbers_list, dif_list):
    return numbers_list[-1] + dif_list[-1]


def find_dif_until_zeros(numbers_list):
    res = [numbers_list.copy()]
    while set(res[-1]) != {0}:
        res.append(find_dif_list(res[-1]))
    return res

def predict_all_numbers(numbers_lists):
    numbers_lists = numbers_lists.copy()
    for i in range(len(numbers_lists) - 1, -1, -1):
        next_number = predict_number(numbers_lists[i], numbers_lists[i - 1])
        numbers_lists[i - 1].append(next_number)
    return numbers_lists[0][-1]

def sum_predictions(lines):
    acc = 0
    for line in lines:
        numbers = [int(n) for n in line.strip().split()][::-1]
        difs= find_dif_until_zeros(numbers)
        acc += predict_all_numbers(difs)
    return acc

if __name__ == '__main__':
    data = open("input/day_9.txt")
    print(sum_predictions(data))
    data.close()

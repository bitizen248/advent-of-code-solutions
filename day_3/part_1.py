from day_3.common import cut_number


def sum_numbers_near_symbols(matrix):
    matrix = [row.copy() for row in matrix]
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            char = matrix[i][j]
            if char.isdigit() or char == ".":
                continue
            if (i - 1) >= 0:
                if matrix[i - 1][j].isdigit():
                    res += cut_number(matrix, (i - 1, j))
                if (j + 1) < len(matrix[i]):
                    if matrix[i - 1][j + 1].isdigit():
                        res += cut_number(matrix, (i - 1, j + 1))
                if (j - 1) >= 0:
                    if matrix[i - 1][j - 1].isdigit():
                        res += cut_number(matrix, (i - 1, j - 1))
            if (j + 1) < len(matrix[i]):
                if matrix[i][j + 1].isdigit():
                    res += cut_number(matrix, (i, j + 1))
            if (j - 1) >= 0:
                if matrix[i][j - 1].isdigit():
                    res += cut_number(matrix, (i, j - 1))
            if (i + 1) < len(matrix):
                if matrix[i + 1][j].isdigit():
                    res += cut_number(matrix, (i + 1, j))
                if (j + 1) < len(matrix[i]):
                    if matrix[i + 1][j + 1].isdigit():
                        res += cut_number(matrix, (i + 1, j + 1))
                if (j - 1) >= 0:
                    if matrix[i + 1][j - 1].isdigit():
                        res += cut_number(matrix, (i + 1, j - 1))
            matrix[i][j] = "."

    return res


if __name__ == "__main__":
    data = open("../input/day_3.txt")
    matrix = [[c for c in line.strip()] for line in data]
    print(sum_numbers_near_symbols(matrix))

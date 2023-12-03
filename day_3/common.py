def cut_number(matrix, cut_position):
    i, j = cut_position
    j_cur = j
    res = matrix[i][j]
    matrix[i][j] = "."
    while j_cur > 0:
        j_cur -= 1
        if matrix[i][j_cur].isdigit():
            res = matrix[i][j_cur] + res
            matrix[i][j_cur] = "."
        else:
            break
    j_cur = j + 1
    while j_cur < len(matrix[i]):
        if matrix[i][j_cur].isdigit():
            res += matrix[i][j_cur]
            matrix[i][j_cur] = "."
        else:
            break
        j_cur += 1

    return int(res)

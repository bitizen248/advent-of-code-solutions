def parse_pipes_map(lines):
    res = []
    lines = lines.readlines()
    lines = [list(line.strip()) for line in lines]
    # lines = [
    #     [c for c in line.split()] for line in
    # ]
    s_point = None
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                s_point = (i, j)
    candidate = {"|", "-", "L", "J", "7", "F"}
    # if lines[s_point[0] - 1][s_point[1]] in ("-", "L", "J"):
    #     candidate -= {"|", "7", "F"}
    # if lines[s_point[0]][s_point[1] + 1] in ("|", "L", "F"):
    #     candidate -= {"-", "F", "7"}
    # if lines[s_point[0] + 1][s_point[1]] in ("7", "-", "F"):
    #     candidate -= {"|", "7", "F"}
    # if lines[s_point[0]][s_point[1] - 1] in ("|", "J", "7"):
    #     candidate -= {"-", "", "F"}
    # print(candidate)
    lines[s_point[0]][s_point[1]] = "J"

    for i, line in enumerate(lines):
        buf = []
        for j, char in enumerate(line):
            dest = None
            if char == "|":
                dest = []
                if i > 0:
                    close = lines[i - 1][j]
                    if close in ("|", "F", "7"):
                        dest.append((i - 1, j))
                if i < len(lines) - 1:
                    close = lines[i + 1][j]
                    if close in ("|", "L", "J"):
                        dest.append((i + 1, j))
            elif char == "-":
                dest = []
                if j > 0:
                    close = lines[i][j - 1]
                    if close in ("-", "L", "F"):
                        dest.append((i, j - 1))
                if j < len(line) - 1:
                    close = lines[i][j + 1]
                    if close in ("-", "J", "7"):
                        dest.append((i, j + 1))
            elif char == "L":
                dest = []
                if i > 0:
                    close = lines[i - 1][j]
                    if close in ("|", "F", "7"):
                        dest.append((i - 1, j))
                if j < len(line) - 1:
                    close = lines[i][j + 1]
                    if close in ("-", "J", "7"):
                        dest.append((i, j + 1))
            elif char == "J":
                dest = []
                if i > 0:
                    close = lines[i - 1][j]
                    if close in ("|", "F", "7"):
                        dest.append((i - 1, j))
                if j > 0:
                    close = lines[i][j - 1]
                    if close in ("-", "L", "F"):
                        dest.append((i, j - 1))
            elif char == "7":
                dest = []
                if i < len(lines) - 1:
                    close = lines[i + 1][j]
                    if close in ("|", "L", "J"):
                        dest.append((i + 1, j))
                if j > 0:
                    close = lines[i][j - 1]
                    if close in ("-", "L", "F"):
                        dest.append((i, j - 1))
            elif char == "F":
                dest = []
                if j < len(line) - 1:
                    close = lines[i][j + 1]
                    if close in ("-", "J", "7"):
                        dest.append((i, j + 1))
                if i < len(lines) - 1:
                    close = lines[i + 1][j]
                    if close in ("|", "L", "J"):
                        dest.append((i + 1, j))
            elif char == ".":
                dest = []
            buf.append(dest)
        res.append(buf)

    return res, s_point


def find_next_point(pipes_map, point):
    i, j = point
    res = []
    if point in pipes_map[i - 1][j]:
        res.append((i - 1, j))
    if point in pipes_map[i + 1][j]:
        res.append((i + 1, j))
    if point in pipes_map[i][j - 1]:
        res.append((i, j - 1))
    if point in pipes_map[i][j + 1]:
        res.append((i, j + 1))
    return res

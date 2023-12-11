def parse_pipes_map(lines):
    res = []
    lines = list(lines)
    s_point = None
    for i, line in enumerate(lines):
        line = line.strip()
        buf = []
        for j, char in enumerate(line):
            dest = None
            if char == "|":
                dest = []
                if i > 0:
                    dest.append((i - 1, j))
                if i < len(lines) - 1:
                    dest.append((i + 1, j))
            elif char == "-":
                dest = []
                if j > 0:
                    dest.append((i, j - 1))
                if j < len(line) - 1:
                    dest.append((i, j + 1))
            elif char == "L":
                dest = []
                if i > 0:
                    dest.append((i - 1, j))
                if j < len(line) - 1:
                    dest.append((i, j + 1))
            elif char == "J":
                dest = []
                if i > 0:
                    dest.append((i - 1, j))
                if j > 0:
                    dest.append((i, j - 1))
            elif char == "7":
                dest = []
                if i < len(lines) - 1:
                    dest.append((i + 1, j))
                if j > 0:
                    dest.append((i, j -1))
            elif char == "F":
                dest = []
                if j < len(line) - 1:
                    dest.append((i, j + 1))
                if i < len(lines) - 1:
                    dest.append((i + 1, j))
            elif char == ".":
                dest = []
            elif char == "S":
                s_point = (i, j)
                dest = None
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


def find_farest_point_in_loop(data):
    pipes_map, s_point = parse_pipes_map(data)
    l_cur, r_cur = find_next_point(pipes_map, s_point)
    visited = {s_point}
    visted_map = dict()
    counter = 1
    end_point = 0
    while l_cur != r_cur:
        # l_cur
        i, j = l_cur
        next_step = pipes_map[i][j]
        visited.add(l_cur)
        visted_map[l_cur] = data[i][j]
        if next_step[0] not in visited:
            l_cur = next_step[0]
        else:
            l_cur = next_step[1]
        end_point = l_cur
        i, j = r_cur
        next_step = pipes_map[i][j]
        visited.add(r_cur)
        if next_step[0] not in visited:
            r_cur = next_step[0]
        else:
            r_cur = next_step[1]

        counter += 1
    return counter

if __name__ == '__main__':
    data = open("input/day_10.txt")
    data = data.readlines()
    res = find_farest_point_in_loop(data)
    print(res)
    visited, s_point, end_point = find_farest_point_in_loop(data)
    print(end_point)
    for i in range(140):
        for j in range(140):
            if end_point == (i, j) and s_point == (i, j):
                print("8", end="")
            elif end_point == (i, j):
                print("E", end="")
            elif s_point == (i, j):
                print("S", end="")
            elif (i, j) in visited:
                print(visited[i,j], end="")
            else:
                print(".", end="")
        print()
    print(len(visited))
    data.close()
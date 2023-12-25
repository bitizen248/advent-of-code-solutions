def read_map(lines):
    res = []
    for i, line in enumerate(lines):
        line = line.strip()
        buf = []
        for j, char in enumerate(line):
            buf.append(char)
        res.append(buf)
    return res


def double_empty_spaces(space):
    rows = []
    for i in range(len(space)):
        is_empty = True
        for char in space[i]:
            if char != ".":
                is_empty = False
                break
        if is_empty:
            rows.append(i)
    size = len(space[0])
    for row in rows[::-1]:
        space = space[0:row] + [["."] * size] + space[row:]

    columns = []
    for j in range(len(space[0])):
        is_empty = True
        for i in range(len(space)):
            if space[i][j] != ".":
                is_empty = False
                break
        if is_empty:
            columns.append(j)

    for column in columns[::-1]:
        for i in range(len(space)):
            space[i] = space[i][0:column] + ["."] + space[i][column:]
    return space

def find_points(space):
    points = []
    for i, line in enumerate(space):
        for j, char in enumerate(line):
            if char == "#":
                points.append((i, j))
    return points

def measure_distance(points):
    destnaces = []
    for i, point1 in enumerate(points[:-1]):
        for point2 in points[i+1:]:
            distance = abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
            destnaces.append(distance)
    return destnaces


if __name__ == '__main__':
    data = open("../input/day_11.txt")
    space = read_map(data)
    space = double_empty_spaces(space)
    points = find_points(space)
    print(sum(measure_distance(points)))

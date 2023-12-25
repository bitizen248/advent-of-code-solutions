from day_11.part_1 import find_points
from day_11.part_1 import read_map


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
        space[row] = ["*"] * size

    columns = []
    for j in range(len(space[0])):
        is_empty = True
        for i in range(len(space)):
            if space[i][j] == "#":
                is_empty = False
                break
        if is_empty:
            columns.append(j)

    for column in columns[::-1]:
        for i in range(len(space)):
            space[i][column] = "*"
    return space

def measure_distance(points):
    destnaces = []
    for i, point1 in enumerate(points[:-1]):
        for point2 in points[i+1:]:
            xn = [point1[0], point2[0]]
            xn.sort()
            x1, x2 = xn
            x_dist = 0
            for i in range(x1, x2):
                if space[i][point1[1]] == "*":
                    x_dist += 1_000_000
                else:
                    x_dist += 1
            yn = [point1[1], point2[1]]
            yn.sort()
            y1, y2 = yn
            y_dist = 0
            for j in range(y1, y2):
                if space[point1[0]][j] == "*":
                    y_dist += 1_000_000
                else:
                    y_dist += 1

            distance = y_dist + x_dist
            destnaces.append(distance)
    return destnaces


if __name__ == '__main__':
    data = open("../input/day_11.txt")
    space = read_map(data)
    space = double_empty_spaces(space)
    for line in space:
        for c in line:
            print(c, end="")
        print()
    points = find_points(space)
    print(sum(measure_distance(points)))

from day_10.common import find_next_point
from day_10.common import parse_pipes_map


def find_farest_point_in_loop(data):
    pipes_map, s_point = parse_pipes_map(data)
    l_cur, r_cur = find_next_point(pipes_map, s_point)
    visited = {s_point}
    visted_map = dict()
    counter = 1
    while l_cur != r_cur:
        i, j = l_cur
        next_step = pipes_map[i][j]
        visited.add(l_cur)
        visted_map[l_cur] = data[i][j]
        if next_step[0] not in visited:
            l_cur = next_step[0]
        else:
            l_cur = next_step[1]
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
    res = find_farest_point_in_loop(data)
    print(res)
    data.close()

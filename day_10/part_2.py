from day_10.common import find_next_point
from day_10.common import parse_pipes_map


def is_connected(pipes_map, point1, point2):
    p1_connectd = point1 in pipes_map[point2[0]][point2[1]]
    p2_connectd = point2 in pipes_map[point1[0]][point1[1]]
    return p1_connectd and p2_connectd


def count_inside_tiles(data):
    pipes_map, s_point = parse_pipes_map(data)
    additional_check = set()
    border = set()
    not_visited = {
        (i, j) for i in range(len(pipes_map)) for j in range(len(pipes_map[0]))
    }
    while not_visited:
        i, j = not_visited.pop()
        next_avaliable = pipes_map[i][j]
        if len(next_avaliable) == 2:
            is_loop = True
            l_cur, _ = next_avaliable
            buf = {(i, j)}
            while True:
                i, j = l_cur
                not_visited -= {(i, j)}
                next_step = pipes_map[i][j]
                if len(next_step) == 1:
                    is_loop = False
                    break
                if next_step[0] not in buf:
                    l_cur = next_step[0]
                elif next_step[1] not in buf:
                    l_cur = next_step[1]
                else:
                    break
                buf.add(l_cur)
            if is_loop:
                border = border.union(buf)
            else:
                additional_check = additional_check.union(buf)
        elif len(next_avaliable) == 1:
            buf = {(i, j)}
            need_to_check = {next_avaliable[0]}
            while need_to_check:
                i, j = need_to_check.pop()
                buf.add((i, j))
                need_to_check = need_to_check.union(
                    {point for point in pipes_map[i][j] if point not in buf})
            not_visited -= buf
            additional_check = additional_check.union(buf)
        elif len(next_avaliable) == 0:
            additional_check.add((i, j))
    outside = {
        (-1, i) for i in range(len(pipes_map[0]))
    }.union({(i, -1) for i in range(len(pipes_map))}).union({
        (len(pipes_map[0]), i) for i in range(len(pipes_map[0]))
    }).union({
        (i, len(pipes_map[0])) for i in range(len(pipes_map))
    })
    for i in range(len(pipes_map)):
        for j in range(len(pipes_map[0])):
            point = (i, j)
            if point in border:
                print("-", end="")
            elif point in additional_check:
                print("I", end="")
            else:
                print("E", end="")
        print()


if __name__ == '__main__':
    map = count_inside_tiles(open('input/day_10.txt'))
    print(map)

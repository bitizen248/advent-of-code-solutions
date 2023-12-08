from math import gcd
from math import lcm

from day_8.part_1 import parse_map


def go_throught_tree(path, tree):
    cur = [key for key in tree.keys() if key[-1] == "A"]
    indexes = {
        "L": 0,
        "R": 1,
    }
    res = []
    for i in range(len(cur)):
        res_buf = 0
        finish = False
        while not finish:
            for way in path:
                index = indexes[way]
                cur[i] = tree[cur[i]][index]
                res_buf += 1
            if cur[i][-1] == "Z":
                res.append(res_buf)
                break

    return res


def find_way(lines):
    path = next(lines).strip()
    next(lines)
    return lcm(*go_throught_tree(path, parse_map(lines)))


if __name__ == "__main__":
    data = open("input/day_8.txt", "r")
    print(find_way(data))
    data.close()

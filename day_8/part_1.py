def parse_map(lines):
    tree = dict()
    for line in lines:
        line = line.strip()
        node, path = line.split(" = ")
        path = path.split(", ")
        left, right = path[0][1:], path[-1][:-1]
        tree[node] = (left, right)
    return tree


def go_throught_tree(path, tree):
    count = 0
    cur = "AAA"
    indexes = {
        "L": 0,
        "R": 1,
    }
    while cur != "ZZZ":
        for way in path:
            index = indexes[way]
            cur = tree[cur][index]
            count += 1
            if cur == "ZZZ":
                break
    return count


def find_way(lines):
    path = next(lines).strip()
    next(lines)
    return go_throught_tree(path, parse_map(lines))


if __name__ == "__main__":
    data = open("input/day_8.txt", "r")
    print(find_way(data))
    data.close()

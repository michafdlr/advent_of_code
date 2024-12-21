from collections import deque
from functools import cache
from itertools import pairwise


def read_file(filename):
    with open(filename, "r") as f:
        codes = f.read()
        codes = codes.splitlines()
    return codes


numeric_pad_neighbors = {
    "A": [("0", "<"), ("3", "^")],
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")]
}
directional_pad_neighbors = {
    "A": [("^", "<"), (">", "v")],
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")]
}
pads = [numeric_pad_neighbors, directional_pad_neighbors]


def get_shortest_paths(start, end, pad):
    queue = deque([(start, [])])
    visited = {start}
    shortest = None
    result = []
    while queue:
        cur, path = queue.popleft()
        if cur == end:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                result.append("".join(path) + "A")
            continue
        if shortest and len(path) >= shortest:
            continue
        for neighbor, direction in pad[cur]:
            visited.add(neighbor)
            queue.append((neighbor, path + [direction]))
    return result


@cache
def get_lengths(code, level, i=0):
    pad = pads[i]
    result = 0
    code = "A" + code
    for start, end in pairwise(code):
        paths = get_shortest_paths(start, end, pad)
        if level == 0:
            result += min(map(len, paths))
        else:
            result += min(get_lengths(path, level - 1, 1) for path in paths)
    return result


def ex1():
    codes = read_file("day21/input.txt")
    return sum(get_lengths(code, 2) * int(code[:-1]) for code in codes)


def ex2():
    codes = read_file("day21/input.txt")
    return sum(get_lengths(code, 25) * int(code[:-1]) for code in codes)


if __name__ == "__main__":
    print(ex1())
    print(ex2())

from queue import PriorityQueue
from collections import deque, defaultdict

def read_file(filename):
    with open(filename, "r") as f:
        codes = f.read()
        codes = codes.splitlines()
    return codes

direction_to_char = {
    (1,0): "v",
    (-1, 0): "^",
    (0, 1): ">",
    (0, -1): "<"
}

char_to_direction = {v: k for (k,v) in direction_to_char.items()}

num_to_pos = {
    "A": (3,2),
    "0": (3,1),
    "1": (2,0),
    "2": (2,1),
    "3": (2,2),
    "4": (1,0),
    "5": (1,1),
    "6": (1,2),
    "7": (0,0),
    "8": (0,1),
    "9": (0,2)
}

arrow_to_pos = {
    "A": (0, 2),
    "^": (0, 1),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

def get_neighbors(pos, keyboard):
    rows, cols = len(keyboard), len(keyboard[0])
    r, c = pos
    neighbors = []
    for dr, dc in direction_to_char:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < rows and 0 <= new_c < cols:
            if rows == 4 and (new_r != 3 or new_c != 0):
                neighbors.append((new_r, new_c))
            elif rows == 2 and (new_r != 0 or new_c != 0):
                neighbors.append((new_r, new_c))
    return neighbors

def build_paths(node, start, predecessors):
    if node == start:
        return [[start]]
    paths = []
    for p in predecessors[node]:
        for subpath in build_paths(p, start, predecessors):
            paths.append(subpath + [node])
    return paths

def find_paths(keyboard, start, end):
    queue = deque([start])
    distance = {start: 0}
    predecessors = defaultdict(list)
    while queue:
        cur = queue.popleft()
        if cur == end:
            break
        for nxt in get_neighbors(cur, keyboard):
            dist = distance[cur] + 1
            if nxt not in distance:
                distance[nxt] = dist
                predecessors[nxt].append(cur)
                queue.append(nxt)
            elif distance[nxt] == dist:
                predecessors[nxt].append(cur)

    if end not in distance:
        return []

    return build_paths(end, start, predecessors)

def get_directions(path):
    dirs = ""
    for i in range(len(path) - 1):
        p2, p1 = path[i + 1], path[i]
        dr, dc =  p2[0] - p1[0], p2[1] - p1[1]
        dirs += direction_to_char[(dr, dc)]
    dirs += "A"
    return dirs

def get_possible_paths(code, keyboard):
    possible_paths = []
    if len(keyboard) == 4:
        cur_pos = num_to_pos["A"]
    else:
        cur_pos = arrow_to_pos["A"]
    for n in code:
        next_pos = num_to_pos[n] if len(keyboard) == 4 else arrow_to_pos[n]
        dirs = []
        paths = find_paths(keyboard, cur_pos, next_pos)
        for path in paths:
            dirs += [get_directions(path)]
        cur_pos = next_pos
        possible_paths += [dirs]
    return possible_paths

def combine_paths(paths_list):
    if not paths_list:
        return []

    def combine(current_paths, remaining_paths):
        if not remaining_paths:
            return current_paths
        next_paths = remaining_paths[0]
        new_paths = []
        for path in current_paths:
            for next_path in next_paths:
                new_paths.append(path + next_path)
        return combine(new_paths, remaining_paths[1:])

    return combine([""], paths_list)

def ex1():
    codes = read_file("day21/input.txt")
    numeric_keyboard = [[7,8,9], [4,5,6], [1,2,3], ["", 0, "A"]]
    directional_keyboard = [["", "^", "A"], ["<", "v", ">"]]
    products = []
    for code in codes:
        possible_num_paths = combine_paths(get_possible_paths(code, numeric_keyboard))
        possible_dir_paths1 = []
        for path in possible_num_paths:
            possible_dir_paths1 += combine_paths(get_possible_paths(path, directional_keyboard))
        min_length = float('inf')
        for path in possible_dir_paths1:
            subpaths = combine_paths(get_possible_paths(path, directional_keyboard))
            for p in subpaths:
                length = len(p)
                min_length = length if length < min_length else min_length
        products.append(min_length*int(code[:-1]))
    return sum(products)


if __name__ == "__main__":
    print(ex1())

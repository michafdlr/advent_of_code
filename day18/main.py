from queue import PriorityQueue

def read_file(filename):
    bytes = []
    with open(filename, "r") as f:
        file = f.readlines()
    bytes = [list(map(int, l.rstrip("\n").split(","))) for l in file]
    return bytes

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def get_corrupted_space(bytes, grid, number_of_bytes):
    for c, r in bytes[:number_of_bytes]:
        grid[r][c] = "#"
    return grid

def debug_print(grid):
    for row in grid:
        print(" ".join(row))

def get_neighbors(pos, grid):
    r, c = pos
    rows, cols = len(grid), len(grid[0])
    neighbors = []
    for dr, dc in directions:
        new_r, new_c = r+dr, c+dc
        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == ".":
            neighbors.append((new_r, new_c))
    return neighbors

def find_shortest_path_pq(grid, start, end):
    queue = PriorityQueue()
    queue.put((0, start))
    scores = {start: 0}
    while not queue.empty():
        prio, cur_pos = queue.get()
        for neighbor in get_neighbors(cur_pos, grid):
            if neighbor == end:
                return prio + 1
            if neighbor not in scores or scores[neighbor] > scores[cur_pos] + 1:
                scores[neighbor] = scores[cur_pos] + 1
                queue.put((scores[neighbor], neighbor))
    return -1

def ex1(rows, cols, bytes):
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    bytes_data = read_file("day18/input.txt")
    grid = get_corrupted_space(bytes_data, grid, bytes)
    start = (0, 0)
    end = (rows - 1, cols - 1)
    shortest_length = find_shortest_path_pq(grid, start, end)
    return shortest_length


def ex2(rows, cols, bytes_start):
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    bytes_data = read_file("day18/input.txt")
    start = (0, 0)
    end = (rows - 1, cols - 1)
    i = bytes_start
    while find_shortest_path_pq(grid, start, end) != -1:
        i += 1
        grid = get_corrupted_space(bytes_data, grid, i)
    return bytes_data[i-1]


if __name__ == "__main__":
    print(ex1(71, 71, 1024))
    print(ex2(71, 71, 1025))

from queue import PriorityQueue
from heapq import heappush, heappop

def read_file(filename):
    bytes = []
    with open(filename, "r") as f:
        file = f.readlines()
    bytes = [list(map(int, l.rstrip("\n").split(","))) for l in file]
    return bytes

rows, cols = 71, 71
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
    neighbors = []
    for dr, dc in directions:
        new_r, new_c = r+dr, c+dc
        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == ".":
            neighbors.append((new_r, new_c))
    return neighbors

def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_shortest_path(grid, start, end):

    open_set = []
    heappush(open_set, (0 + manhattan(start, end), 0, start))
    g_score = {start: 0}

    while open_set:
        _, current_cost, current = heappop(open_set)

        if current == end:
            return current_cost

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                priority = tentative_g_score + manhattan(neighbor, end)
                heappush(open_set, (priority, tentative_g_score, neighbor))

    return -1  # Path not found

def ex1():
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    bytes_data = read_file("day18/input.txt")
    grid = get_corrupted_space(bytes_data, grid, 1024)
    start = (0, 0)  # Replace with actual start position
    end = (rows - 1, cols - 1)  # Replace with actual end position
    shortest_length = find_shortest_path(grid, start, end)
    return shortest_length

if __name__ == "__main__":
    print(ex1())

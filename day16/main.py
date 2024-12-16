from queue import PriorityQueue
from collections import deque

def read_file(filename):
    with open(filename, "r") as f:
        file = f.read()
        grid = file.splitlines()
        grid = [list(row) for row in grid]
    return grid

def debug_print(grid):
    for row in grid:
        print(" ".join(row))

def find_start_and_end(grid):
    start, end = None, None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                start = row, col
            if grid[row][col] == "E":
                end = row, col
            if start and end:
                return start, end


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_prio(previous, current, next):
    if current in previous:
        last = previous[current]
        if abs(next[0] - last[0]) == 1:
            return 1000
    return 1

def get_possible_moves(pos, grid, visited, previous):
    moves = []
    row, col = pos
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if grid[new_row][new_col] != "#" and (new_row, new_col) not in visited:
            prio = get_prio(previous, (row, col), (new_row, new_col))
            moves.append((prio, (new_row, new_col)))
    moves.sort(key=lambda x: x[0])
    return moves

def solve_maze(grid, start, end):
    queue = PriorityQueue()
    cur_pos = start
    queue.put((0, cur_pos))
    visited = {start}
    previous = {}
    while not queue.empty():
        prio_old, cur_pos = queue.get()
        visited.add(cur_pos)
        next_positions = get_possible_moves(cur_pos, grid, visited, previous)
        for prio, pos in next_positions:
            if pos not in visited:
                visited.add(pos)
                previous[pos] = cur_pos
                queue.put((prio_old + prio, pos))
            if pos == end:
                path = retrace(previous, start, end)
                return path

def print_solved_grid(path, grid):
    for (row, col) in path:
        grid[row][col] = "x"
    debug_print(grid)

def retrace(previous, start, end):
    path = deque()
    current = end
    while current != start:
        path.appendleft(current)
        current = previous.get(current)
        if current is None:
            return None
    path.appendleft(start)
    return list(path)


def ex1():
    grid = read_file("day16/testinput.txt")
    #debug_print(grid)
    #print("\n\n")
    start, end = find_start_and_end(grid)
    path = solve_maze(grid, start, end)
    #print(path)
    forward = 0
    turn = 0
    previous = None
    for i in range(len(path) - 1):
        if i == 0:
            if path[i+1][1] - path[i][1] == 1:
                forward += 1
                previous = (0,1)
            else:
                turn += 1
                previous = (path[i+1][0] - path[i][0], path[i+1][1] - path[i][1])
                forward += 1
        else:
            if previous:
                if path[i+1][0] - path[i][0] == previous[0] and path[i+1][1] - path[i][1] == previous[1]:
                    forward += 1
                else:
                    turn += 1
                    previous = (path[i+1][0] - path[i][0], path[i+1][1] - path[i][1])
                    forward += 1
    return forward + 1000*turn

################## PART 2 #####################################


if __name__ == "__main__":
    print(ex1())

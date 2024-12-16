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
            return 1001
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
                return prio_old + 1

def print_solved_grid(path, grid):
    for (row, col) in path:
        grid[row][col] = "x"
    debug_print(grid)

def ex1():
    grid = read_file("day16/input.txt")
    start, end = find_start_and_end(grid)
    return solve_maze(grid, start, end)

################## PART 2 #####################################

def solve_maze_optimized(grid, start, end):
    queue = PriorityQueue()
    queue.put((0, start, None))  # (cost, position, last_direction)


    min_cost = {}

    predecessors = {}

    while not queue.empty():
        cost, pos, last_dir = queue.get()
        state = (pos, last_dir)

        if state in min_cost and cost > min_cost[state]:
            continue

        min_cost[state] = cost

        if pos == end:
            continue

        row, col = pos
        for idx, (dr, dc) in enumerate(directions):
            new_row, new_col = row + dr, col + dc
            new_pos = (new_row, new_col)

            if grid[new_row][new_col] != "#":
                if last_dir is not None and last_dir != idx:
                    move_cost = 1001
                else:
                    move_cost = 1
                new_cost = cost + move_cost
                new_state = (new_pos, idx)

                if new_state in min_cost and new_cost > min_cost[new_state]:
                    continue

                if new_state not in predecessors:
                    predecessors[new_state] = set()
                predecessors[new_state].add(state)

                queue.put((new_cost, new_pos, idx))

    minimal_total_cost = min(
        min_cost[state] for state in min_cost if state[0] == end
    )

    end_states = [
        state for state in min_cost
        if state[0] == end and min_cost[state] == minimal_total_cost
    ]

    positions_in_optimal_paths = set()
    visited_states = set()
    stack = end_states.copy()
    while stack:
        current_state = stack.pop()
        if current_state in visited_states:
            continue
        visited_states.add(current_state)
        pos, _ = current_state
        positions_in_optimal_paths.add(pos)
        if current_state in predecessors:
            for prev_state in predecessors[current_state]:
                stack.append(prev_state)

    return positions_in_optimal_paths

def ex2():
    grid = read_file("day16/input.txt")
    start, end = find_start_and_end(grid)
    positions_in_optimal_paths = solve_maze_optimized(grid, start, end)
    return len(positions_in_optimal_paths)

if __name__ == "__main__":
    print(ex1(), end="\n")
    print(ex2())

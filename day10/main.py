def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = list(map(int, lines[i].rstrip()))
    return lines

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def check_ways(pos, grid):
    cur_row, cur_col = pos
    next_positions = []
    rows, cols = len(grid), len(grid[0])
    for (row, col) in directions:
        new_row, new_col = cur_row + row, cur_col + col
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == grid[cur_row][cur_col] + 1:
            next_positions.append((new_row, new_col))
    return next_positions

def find_trailheads(grid):
    trailheads = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                trailheads.append((row, col))
    return trailheads



def ex1():
    grid = read_file("day10/input.txt")
    trailheads = find_trailheads(grid)
    score = 0
    for trailhead in trailheads:
        queue = [trailhead]
        visited_endpoints = set()
        while queue:
            cur_pos = queue.pop()
            if grid[cur_pos[0]][cur_pos[1]] == 9:
                if not cur_pos in visited_endpoints:
                    visited_endpoints.add(cur_pos)
                    score += 1
            else:
                new_pos = check_ways(cur_pos, grid)
                for pos in new_pos:
                    queue.append(pos)
    return score

def ex2():
    grid = read_file("day10/input.txt")
    trailheads = find_trailheads(grid)
    score = 0
    for trailhead in trailheads:
        queue = [trailhead]
        while queue:
            cur_pos = queue.pop()
            if grid[cur_pos[0]][cur_pos[1]] == 9:
                score += 1
            else:
                new_pos = check_ways(cur_pos, grid)
                for pos in new_pos:
                    queue.append(pos)
    return score

if __name__ == "__main__":
    print(ex2())

from utils import read_file
from collections import defaultdict

def ex1():
    directions = {"^": [[-1, 0], ">"], "v": [[1,0], "<"], ">": [[0, 1], "v"], "<": [[0, -1], "^"]}
    grid = read_file("day6/input.txt")
    rows, cols = len(grid), len(grid[0])
    position = []
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in directions:
                visited.add((i,j))
                position = [[i,j], directions[grid[i][j]]]
                break

    while 0<position[0][0]<rows-1 and 0<position[0][1]<cols-1:
        if grid[position[0][0] + position[1][0][0]][position[0][1] + position[1][0][1]] == "#":
            position[1] = directions[position[1][1]]
        else:
            position[0] = [position[0][0] + position[1][0][0], position[0][1] + position[1][0][1]]
            visited.add(tuple(position[0]))
    return len(visited)


def ex2():
    grid = read_file("day6/input.txt")
    rows = len(grid)
    cols = len(grid[0])

    grid = [[c for c in line] for line in grid]
    directions = { '^': 0, '>': 1, 'v': 2, '<': 3 }

    result_two = 0

    start = None
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] not in ['.', '#']:
                start = (y, x, directions[grid[y][x]])
                grid[y][x] = '.'
                break
        if start:
            break

    for block_y in range(rows):
        for block_x in range(cols):
            if (block_y, block_x) == (start[0], start[1]):
                continue
            if grid[block_y][block_x] == '#':
                continue
            grid[block_y][block_x] = '#'
            visited = defaultdict(list)
            y, x = (start[0], start[1])
            direction = start[2]
            while True:
                if direction == 0:
                    new_y, new_x = (y-1, x)
                elif direction == 1:
                    new_y, new_x = (y, x+1)
                elif direction == 2:
                    new_y, new_x = (y+1, x)
                elif direction == 3:
                    new_y, new_x = (y, x-1)

                if new_y < 0 or new_x < 0 or new_y >= rows or new_x >= cols:
                    grid[block_y][block_x] = '.'
                    break

                if grid[new_y][new_x] != '#':
                    visited[(y, x)].append(direction)
                    y = new_y
                    x = new_x
                else:
                    direction = (direction + 1) % 4

                if direction in visited[(y, x)]:
                    result_two += 1
                    grid[block_y][block_x] = '.'
                    break
            grid[block_y][block_x] = '.'


    return result_two

if __name__ == "__main__":
    print(ex2())

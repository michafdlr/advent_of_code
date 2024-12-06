from utils import read_file

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
    while 0<position[0][0]<rows-1 and 0<position[0][1]<cols-1:
        if grid[position[0][0] + position[1][0][0]][position[0][1] + position[1][0][1]] == "#":
            position[1] = directions[position[1][1]]
        else:
            position[0] = [position[0][0] + position[1][0][0], position[0][1] + position[1][0][1]]
            visited.add(tuple(position[0]))
    return len(visited)


if __name__ == "__main__":
    print(ex1())

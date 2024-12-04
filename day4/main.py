from utils import read_file
from itertools import permutations

def ex1():
    grid = read_file("day4/input.txt")
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    count = 0

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          (0, 1),
                  ( 1, -1), ( 1, 0), (1, 1)]

    def search(x, y, dx, dy):
        for k in range(len(word)):
            nx, ny = x + k * dx, y + k * dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == word[k]:
                continue
            return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search(i, j, dx, dy):
                    count += 1
    return count


def ex2():
    grid = read_file("day4/input.txt")
    rows, cols = len(grid), len(grid[0])
    count = 0

    def check_sequence(i, j):
        if i == 0 or i==rows-1 or j==0 or j==cols-1:
            return False
        d1 = grid[i-1][j-1] + grid[i][j] +grid[i+1][j+1]
        d2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
        if (d1 == "MAS" and d2=="MAS") or (d1 == "SAM" and d2 == "MAS") or (d1 == "MAS" and d2 == "SAM") or (d1 == "SAM" and d2 == "SAM"):
            return True
        return False

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                if check_sequence(i,j):
                    count += 1
    return count


if __name__ == "__main__":
    print(ex2())

from utils import read_file

def get_distance(pos1, pos2):
    return pos2[0] - pos1[0], pos2[1] - pos1[1]

def check_bounds(pos, rows, cols):
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols

def ex1():
    grid = read_file("day8/input.txt")
    rows, cols = len(grid), len(grid[0])

    antennas = {}
    antinodes = set()
    for row in range(rows):
        for col in range(cols):
            el = grid[row][col]
            if el != ".":
                if el in antennas:
                    for pos in antennas[el]:
                        dx, dy = get_distance(pos, (row, col))
                        antinode_1 = (row + dx, col + dy)
                        antinode_2 = (pos[0] - dx, pos[1] - dy)
                        if check_bounds(antinode_1, rows, cols):
                            antinodes.add(antinode_1)
                        if check_bounds(antinode_2, rows, cols):
                            antinodes.add(antinode_2)
                    antennas[el].append((row,col))
                else:
                    antennas[el] = [(row,col)]

    return len(antinodes)

def ex2():
    grid = read_file("day8/input.txt")
    rows, cols = len(grid), len(grid[0])

    antennas = {}
    antinodes = set()
    for row in range(rows):
        for col in range(cols):
            el = grid[row][col]
            if el != ".":
                if el in antennas:
                    for pos in antennas[el]:
                        dx, dy = get_distance(pos, (row, col))
                        antinode = (row + dx, col + dy)
                        while check_bounds(antinode, rows, cols):
                            antinodes.add(antinode)
                            antinode = (antinode[0] + dx, antinode[1] + dy)
                        antinode = (pos[0] - dx, pos[1] - dy)
                        while check_bounds(antinode, rows, cols):
                            antinodes.add(antinode)
                            antinode = (antinode[0] - dx, antinode[1] - dy)
                    antennas[el].append((row,col))
                else:
                    antennas[el] = [(row,col)]
    antenna_positions = set()
    for pos in antennas.values():
        for el in pos:
            antenna_positions.add(el)
    return len(antinodes) + sum((len(antennas[pos]) for pos in antennas if len(antennas[pos])>1)) - len(antinodes & antenna_positions)

if __name__ == "__main__":
    print(ex2())

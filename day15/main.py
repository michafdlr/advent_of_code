def read_file(filename):
    with open(filename, "r") as f:
        file = f.read()
        file = file.rstrip("\n")
        file = file.split("\n\n")
        robot_map, moves = list(map(list, file[0].splitlines())), file[1].replace("\n", "")
    return robot_map, moves


def find_element(robot_map, element):
    rows, cols = len(robot_map), len(robot_map[0])
    row, col = 1, 1
    val = robot_map[row][col]
    if element == "@":
        while val != element:
            if col < cols - 2:
                col += 1
                val = robot_map[row][col]
            elif col == cols - 2 and row < rows - 2:
                row, col = row + 1, 1
                val = robot_map[row][col]
            elif row == rows - 2:
                raise IndexError
        return row, col
    else:
        boxes = []
        for row in range(rows-1):
            for col in range(cols-1):
                if robot_map[row][col] == element:
                    boxes.append((row, col))
        return boxes


direction_map = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

def look_direction(pos, direction, robot_map):
    row, col = pos
    dr, dc = direction_map[direction]
    new_row, new_col = row + dr, col + dc
    new_val = robot_map[new_row][new_col]
    return (new_row, new_col), new_val

def move_parts(pos, direction, robot_map):
    row, col = pos
    robot = pos
    dr, dc = direction_map[direction]
    new_row, new_col = row + dr, col + dc
    new_val = robot_map[new_row][new_col]
    if new_val == "#":
        return robot_map, robot
    if new_val == ".":
        robot_map[row][col] = "."
        robot_map[new_row][new_col] = "@"
        robot = new_row, new_col
        return robot_map, robot
    if new_val == "O":
        moved_parts = [(new_row, new_col)]
        while look_direction((new_row, new_col), direction, robot_map)[-1] == "O":
            moved_parts.append((new_row, new_col))
            (new_row, new_col), new_val = look_direction((new_row, new_col), direction, robot_map)
        (new_row, new_col), new_val = look_direction((new_row, new_col), direction, robot_map)
        if new_val == ".":
            moved_parts.append((new_row, new_col))
            robot_map[robot[0]][robot[1]] = "."
            robot = moved_parts[0]
            for i in range(len(moved_parts)):
                row, col = moved_parts[i]
                if i == 0:
                    robot_map[row][col] = "@"
                else:
                    robot_map[row][col] = "O"
        return robot_map, robot


def ex1():
    robot_map, moves = read_file("day15/input.txt")
    robot = find_element(robot_map, "@")
    for move in moves:
        robot_map, robot = move_parts(robot, move, robot_map)
    boxes = find_element(robot_map, "O")
    sum_coordinates = sum(100*box[0] + box[1] for box in boxes)
    return sum_coordinates


def ex2():
    return

if __name__ == "__main__":
    print(ex1())

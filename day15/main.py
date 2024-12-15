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

################## PART 2 #####################################

replace_map = {"#": 2*["#"], "O": ["[", "]"], ".": 2*["."], "@": ["@", "."]}

def rebuild_map(robot_map):
    rows, cols = len(robot_map), len(robot_map[0])
    new_map = [[] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            new_map[row] += replace_map[robot_map[row][col]]
    return new_map

def debug_print(robot_map):
    for line in robot_map:
        print("".join(line))

def try_move(robot_map, pos, dpos):
    row, col = pos
    dr, dc = dpos
    new_row, new_col = row + dr, col + dc
    if robot_map[new_row][new_col] == "#":
        return False
    elif robot_map[new_row][new_col] == ".":
        return True
    if dc == 0:
        if robot_map[new_row][new_col] == "]":
            return try_move(robot_map, (new_row, new_col), dpos) and try_move(
                robot_map, (new_row, new_col - 1), dpos
            )
        elif robot_map[new_row][new_col] == "[":
            return try_move(robot_map, (new_row, new_col), dpos) and try_move(
                robot_map, (new_row, new_col + 1), dpos
            )
    elif dc == -1:
        if robot_map[new_row][new_col] == "]":
            return try_move(robot_map, (new_row, new_col - 1), dpos)
    elif dc == 1:
        if robot_map[new_row][new_col] == "[":
            return try_move(robot_map, (new_row, new_col + 1), dpos)
    return False

def move_robot(robot_map, pos, dpos):
    row, col = pos
    dr, dc = dpos
    new_row, new_col = row + dr, col + dc
    if robot_map[new_row][new_col] == "#":
        return
    elif robot_map[new_row][new_col] == ".":
        robot_map[row][col], robot_map[new_row][new_col] = robot_map[new_row][new_col], robot_map[row][col]
        return
    if dc == 0:
        if robot_map[new_row][new_col] == "]":
            move_robot(robot_map, (new_row, new_col), dpos)
            move_robot(robot_map, (new_row, new_col - 1), dpos)
            robot_map[row][col], robot_map[new_row][new_col] = robot_map[new_row][new_col], robot_map[row][col]
        elif robot_map[new_row][new_col] == "[":
            move_robot(robot_map, (new_row, new_col), dpos)
            move_robot(robot_map, (new_row, new_col + 1), dpos)
            robot_map[row][col], robot_map[new_row][new_col] = robot_map[new_row][new_col], robot_map[row][col]
    elif dc == -1:
        if robot_map[new_row][new_col] == "]":
            move_robot(robot_map, (new_row, new_col - 1), dpos)
            robot_map[new_row][new_col - 1], robot_map[new_row][new_col], robot_map[row][col] = (
                robot_map[new_row][new_col],
                robot_map[row][col],
                robot_map[new_row][new_col - 1],
            )
    elif dc == 1:
        if robot_map[new_row][new_col] == "[":
            move_robot(robot_map, (new_row, new_col + 1), dpos)
            robot_map[new_row][new_col + 1], robot_map[new_row][new_col], robot_map[row][col] = (
                robot_map[new_row][new_col],
                robot_map[row][col],
                robot_map[new_row][new_col + 1],
            )

def ex2():
    robot_map, moves = read_file("day15/input.txt")
    robot_map = rebuild_map(robot_map)
    robot = find_element(robot_map, "@")
    for move in moves:
        dpos = direction_map[move]
        if try_move(robot_map, robot, dpos):
            move_robot(robot_map, robot, dpos)
            robot = (robot[0] + dpos[0], robot[1] + dpos[1])
    boxes = find_element(robot_map, "[")
    sum_coordinates = sum(100*box[0] + box[1] for box in boxes)
    return sum_coordinates

if __name__ == "__main__":
    print(ex2())

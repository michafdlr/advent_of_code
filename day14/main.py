def read_file(filename):
    robots = []
    with open(filename, "r") as f:
        file = f.readlines()
    for line in file:
        robot = {}
        line = line.split()
        robot["p"] = tuple(map(int, line[0].strip("p=").split(",")))
        robot["v"] = tuple(map(int, line[1].strip("v=").split(",")))
        robots.append(robot)
    return robots

width, height = 101, 103
mid_x, mid_y = width // 2, height // 2



def robot_move(p, v):
    x, y = p
    v_x, v_y = v
    new_x, new_y = x+v_x, y+v_y
    if new_x >= width:
        new_x -= width
    elif new_x < 0:
        new_x += width
    if new_y >= height:
        new_y -= height
    elif new_y < 0:
        new_y += height
    return new_x, new_y

def count_robots_quadrant(robots):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        x, y = robot["p"]
        if 0 <= x < mid_x:
            if 0 <= y < mid_y:
                q1 += 1
            elif y > mid_y:
                q3 += 1
        elif mid_x < x:
            if 0 <= y < mid_y:
                q2 += 1
            elif y > mid_y:
                q4 += 1
    return q1 * q2 * q3 * q4

def ex1():
    robots = read_file("day14/input.txt")
    for robot in robots:
        for _ in range(100):
            p, v = robot["p"], robot["v"]
            robot["p"] = robot_move(p, v)
    return count_robots_quadrant(robots)


def check_duplicates(robots):
    allocated = []
    i = 0
    p = robots[i]["p"]
    while p not in allocated and i < len(robots)-1:
        allocated.append(p)
        i += 1
        p = robots[i]["p"]
    return i == len(robots) - 1

def ex2():
    robots = read_file("day14/input.txt")
    seconds = 0
    while not check_duplicates(robots):
        seconds += 1
        for robot in robots:
            p, v = robot["p"], robot["v"]
            robot["p"] = robot_move(p, v)
    return seconds

if __name__ == "__main__":
    print(ex2())

from queue import PriorityQueue

def read_file(filename):
    with open(filename, "r") as f:
        file = f.read()
        grid = file.splitlines()
        grid = [list(row) for row in grid]
    return grid

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

def debug_print(grid):
    for line in grid:
        print(" ".join(line))


def get_neighbors(pos, grid):
    rows, cols = len(grid), len(grid[0])
    r, c = pos
    neighbors = []
    for dr, dc in directions:
        new_r, new_c = r+dr, c+dc
        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != "#":
            neighbors.append((new_r, new_c))
    return neighbors

def find_shortest_path(grid, start, end):
    queue = PriorityQueue()
    queue.put((0, start))
    scores = {start: 0}
    previous = {}
    while not queue.empty():
        _, cur_pos = queue.get()
        for neighbor in get_neighbors(cur_pos, grid):
            if neighbor == end:
                previous[neighbor] = cur_pos
                scores[neighbor] = scores[cur_pos] + 1
                return scores, previous
            if neighbor not in scores or scores[neighbor] > scores[cur_pos] + 1:
                scores[neighbor] = scores[cur_pos] + 1
                previous[neighbor] = cur_pos
                queue.put((scores[neighbor], neighbor))
    return

def get_path(previous, start, end):
    path = [end]
    cur = end
    while cur != start:
        cur = previous[cur]
        path = [cur] + path
    return path

def ex1():
    grid = read_file("day20/input.txt")
    start, end = find_start_and_end(grid)
    scores, _ = find_shortest_path(grid, start, end)
    return sum((row+2*dr,col+2*dc) in scores and scores[(row,col)]+102<=scores[(row+2*dr,col+2*dc)] for row,col in scores for dr,dc in directions)



#################### PART 2 ############################
def manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def get_shortcuts(path, i , max_time = 20, min_saved = 100):
    positions = set()
    j = i+min_saved+2
    while j < len(path):
        dist = manhattan_dist(path[i],path[j])
        gain = j - i - manhattan_dist(path[i],path[j])
        if dist<=max_time and gain>=min_saved:
            steps = max_time-dist+1
            for k in range(min(len(path)-j, steps)):
                positions.add(path[j+k])
            j += steps
        elif dist<=max_time:
            j += (min_saved+1-gain)//2
        else:
            j += dist-max_time
    return positions

def calc_shortcuts(path, scores, max_time=20, min_saved=100):
    s = get_shortcuts(path,0,max_time,min_saved)
    positions = len(s)
    for i in range(1,len(path)-min_saved-2):
        row, col, new_row, new_col = *path[i-1], *path[i]
        dr, dc = new_row-row,new_col-col
        s.discard(path[i+min_saved+1])
        for j in range(-max_time,max_time+1):
            der, dec = dr*(max_time-abs(j))+dc*j, dc*(max_time-abs(j))+dr*j
            s.discard((row-der, col-dec))
            ner,nec = (new_row+der, new_col+dec)
            if (ner,nec) in scores:
                k = scores[(ner,nec)]
                if k - i - manhattan_dist(path[i], (ner,nec)) >= min_saved:
                    s.add((ner,nec))
        for j in range(i+min_saved+1, min(len(path), i+min_saved+max_time)):
            if j - i - manhattan_dist(path[i], path[j]) < min_saved:
                s.discard(path[j])
        positions += len(s)
    return positions


def ex2():
    grid = read_file("day20/input.txt")
    start, end = find_start_and_end(grid)
    scores, previous = find_shortest_path(grid, start, end)
    path = get_path(previous, start, end)
    return calc_shortcuts(path, scores, 20, 100)


if __name__ == "__main__":
    print(ex1())
    print(ex2())

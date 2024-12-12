def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = list(lines[i].rstrip())
    return lines

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def check_bounds(pos, rows, cols):
    r, c = pos
    return 0 <= r < rows and 0 <= c < cols

def get_neighbors(grid, pos, letter):
    rows, cols = len(grid), len(grid[0])
    neighbor_count = 0
    neighbors = set()
    r, c = pos
    for direction in directions:
        new_r, new_c = r + direction[0], c + direction[1]
        new_pos = (new_r, new_c)
        if check_bounds(new_pos, rows, cols):
            if grid[new_r][new_c] == letter:
                neighbors.add(new_pos)
                neighbor_count += 1
    return neighbors, 4-neighbor_count

def get_region(grid, pos, letter, not_visited):
    region = set()
    perimeter = 0
    queue = [pos]
    while queue:
        cur_pos = queue.pop()
        region.add(cur_pos)
        not_visited.remove(cur_pos)
        neighbors, perim_add = get_neighbors(grid, cur_pos, letter)
        perimeter += perim_add
        for neighbor in neighbors:
            if neighbor in region:
                continue
            else:
                region.add(neighbor)
                queue.append(neighbor)
    return region, perimeter*len(region)

def get_perimeter():
    pass

def ex1():
    grid = read_file("day12/input.txt")
    rows, cols = len(grid), len(grid[0])
    not_visited = [(r, c) for r in range(rows) for c in range(cols)]
    regions = []
    total_price = 0
    while not_visited:
        pos = not_visited[0]
        region, price = get_region(grid, pos, grid[pos[0]][pos[1]], not_visited)
        regions.append(region)
        total_price += price
    return total_price

def ex2():
    return

if __name__ == "__main__":
    print(ex1())

from functools import cache

def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
        data = list(map(int,data.strip().split(" ")))
    return data

def blink(stones):
    new_stones = []
    for stone in stones:
        stone_length = len(str(stone))
        if stone == 0:
            new_stones.append(1)
        elif stone_length % 2 == 0:
            new_stones.append(int(str(stone)[:stone_length//2]))
            new_stones.append(int(str(stone)[stone_length//2:]))
        else:
            new_stones.append(2024*stone)
    return new_stones



def ex1():
    stones = read_file("day11/input.txt")
    for i in range(25):
        stones = blink(stones)
    return len(stones)

@cache
def get_count(stone, i):
    if i == 0:
        return 1
    if stone == 0:
        return get_count(1, i-1)
    if (length := len(str(stone))) % 2 == 0:
        return get_count(int(str(stone)[:length//2]), i-1) + get_count(int(str(stone)[length//2:]), i-1)
    return get_count(stone * 2024, i-1)

def ex2():
    stones = read_file("day11/input.txt")
    return sum(get_count(stone, 75) for stone in stones)

if __name__ == "__main__":
    print(ex2())

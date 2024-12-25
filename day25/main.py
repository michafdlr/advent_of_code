import time
from typing import NamedTuple

def read_file(filename):
    with open(filename, "r") as f:
        parts = f.read().rstrip("\n").split("\n\n")
    for i, part in enumerate(parts):
        parts[i] = list(part.splitlines())
    locks, keys = [], []
    for part in parts:
        if part[0][0] == "#":
            locks.append(part)
        else:
            keys.append(tuple(part))
    return locks, keys


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Time needed for function {func.__name__}: {end-start:.2f} sec\n")
        return result
    return wrapper

def find_heights(element):
    heights = [0 for _ in range(len(element[0]))]
    for row in range(len(element)):
        for col in range(len(element[0])):
            if element[row][col] == "#":
                heights[col] += 1
    return tuple(heights)

@timer
def ex1():
    locks, keys = read_file("day25/input.txt")
    total = 0
    key_heights = {}
    for lock in locks:
        l_heights = find_heights(lock)
        for key in keys:
            if key in key_heights:
                k_heights = key_heights[key]
            else:
                k_heights = find_heights(key)
            if all(l_heights[i] + k_heights[i] <= 7  for i in range(len(l_heights))):
                total += 1
            else:
                key_heights[key] = k_heights
    return total


if __name__ == "__main__":
    print(f"Solution 1: {ex1()}\n", end=f"{20*'-'}\n")

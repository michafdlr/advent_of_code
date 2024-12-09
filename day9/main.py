def read_file(filename):
    with open(filename, "r") as f:
        diskmap = f.read().strip()
    return diskmap

def get_file_block(diskmap):
    id = 0
    file_block = []
    for i in range(len(diskmap)):
        if i%2 == 0:
            file_block += int(diskmap[i])*[str(id)]
            id += 1
        else:
            file_block += int(diskmap[i])*["."]
    return file_block

def rearange(file_block):
    file_len = len(file_block)
    i = 0
    last_idx = file_len - 1
    while i<file_len:
        while file_block[last_idx] == "." and last_idx > i:
                last_idx -= 1
        if last_idx == i:
            return file_block[:i+1]
        if file_block[i] == ".":
            file_block[i], file_block[last_idx] = file_block[last_idx], file_block[i]
            last_idx -= 1
        i += 1

def ex1():
    diskmap = read_file("day9/input.txt")
    file_block = get_file_block(diskmap)
    rearanged_block = rearange(file_block)
    return sum(i * int(rearanged_block[i]) for i in range(len(rearanged_block)))

## part 2

def find_file(file_block, file_idx):
    for idx, file in reversed(list(enumerate(file_block))):
        if file[0] == "File" and file[2] == file_idx:
            return idx


def find_free_space(file_block, size_required, file_idx):
    for idx, (file_type, file_size, _) in enumerate(file_block):
        if file_type == "File":
            continue

        if idx >= file_idx:
            return False

        if file_size >= size_required:
            return idx

    return False


def move_file(file_block, file_idx, free_space_idx):
    file = file_block[file_idx]
    free_space = file_block[free_space_idx]

    file_block[file_idx] = ("Free", file[1], 0)
    file_block[free_space_idx] = file

    free_space_remaining = free_space[1] - file[1]
    if free_space_remaining:
        file_block.insert(free_space_idx + 1, ("Free", free_space_remaining, 0))

    return file_block


def build_file_p2(input):
    file_block = []
    is_file = True
    idx = 0

    for i in input:
        if is_file:
            file_block.append(("File", int(i), idx))
            idx += 1

        if not is_file:
            file_block.append(("Free", int(i), 0))

        is_file = not is_file

    for i in reversed(range(idx)):
        idx = find_file(file_block, i)
        _, file_size, _ = file_block[idx]

        free_space_idx = find_free_space(file_block, file_size, idx)

        if free_space_idx:
            file_block = move_file(file_block, idx, free_space_idx)

    flattened = []

    for _, file_size, file_idx in file_block:
        for _ in range(file_size):
            flattened.append(file_idx)

    return flattened


def ex2():
    diskmap = read_file("day9/testinput.txt")
    rearanged_block = build_file_p2(diskmap)
    return sum(i * int(rearanged_block[i]) for i in range(len(rearanged_block)))


if __name__ == "__main__":
    print(ex2())

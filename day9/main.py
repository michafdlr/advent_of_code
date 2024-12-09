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
    # checksum = 0
    # for i, el in enumerate(rearanged_block):
    #     if el == ".":
    #         return checksum
    #     else:
    #         checksum += i*int(el)


if __name__ == "__main__":
    print(ex1())

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = list(lines[i].rstrip())
    return lines

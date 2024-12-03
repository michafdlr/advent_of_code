def read_file(filename):
    with open(filename, "r") as f:
        string = f.read()
        string.strip()
    return string

def read_file(filename):
    test_values = []
    values = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(": ")
            test_values.append(int(line[0]))
            values.append(list(map(int, line[1].split(" "))))
    return test_values, values

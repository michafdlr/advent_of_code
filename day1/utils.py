def read_file(filename):
    with open(filename, "r+") as f:
        lines = f.readlines()
        print(lines[:10])
        list_1 = []
        list_2 = []
        for line in lines:
            line = line.rstrip().split()
            list_1.append(int(line[0]))
            list_2.append(int(line[-1]))
    return list_1, list_2

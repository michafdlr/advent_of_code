def read_file_to_lists(filename):
    with open(filename, "r+") as f:
        lines = f.readlines()
        list_1 = []
        list_2 = []
        for line in lines:
            line = line.rstrip().split()
            list_1.append(int(line[0]))
            list_2.append(int(line[-1]))
    return list_1, list_2

def read_file_to_dicts(filename):
    with open(filename, "r+") as f:
        lines = f.readlines()
        dict_1 = {}
        dict_2 = {}
        for line in lines:
            line = line.rstrip().split()
            dict_1[line[0]] = 1 if line[0] not in dict_1 else dict_1[line[0]] + 1
            dict_2[line[1]] = 1 if line[1] not in dict_2 else dict_2[line[1]] + 1
    return dict_1, dict_2

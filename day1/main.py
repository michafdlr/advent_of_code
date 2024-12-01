from utils import read_file_to_lists, read_file_to_dicts

def ex1():
    list_1, list_2 = read_file_to_lists("day1/input.txt")
    list_1.sort()
    list_2.sort()
    print(list_1[-10:], list_2[-10:])
    sum_of_distances = 0
    for i in range(len(list_1)):
        sum_of_distances += abs(list_1[i]-list_2[i])
    return sum_of_distances

def ex2():
    dict_1, dict_2 = read_file_to_dicts("day1/input.txt")
    similarity_score = 0
    for num in dict_1:
        if num in dict_2:
            similarity_score += int(num) * dict_1[num] * dict_2[num]
    return similarity_score

if __name__ == "__main__":
    print(ex1())
    print(ex2())

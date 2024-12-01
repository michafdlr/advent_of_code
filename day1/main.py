from utils import read_file

def main():
    list_1, list_2 = read_file("day1/input.txt")
    list_1.sort()
    list_2.sort()
    print(list_1[-10:], list_2[-10:])
    sum_of_distances = 0
    for i in range(len(list_1)):
        sum_of_distances += abs(list_1[i]-list_2[i])
    return sum_of_distances


if __name__ == "__main__":
    print(main())

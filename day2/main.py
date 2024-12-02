from utils import read_file

def check_monotonicity(report):
    if abs(report[0] - report[1]) > 3:
        return False

    is_monotone = True
    increasing = report[0] < report[1]
    index = 0

    while is_monotone and index < len(report) - 1:
        if abs(report[index] - report[index + 1]) > 3:
            return False
        if increasing and report[index] >= report[index + 1]:
            return False
        if not increasing and report[index] <= report[index + 1]:
            return False
        index += 1
    return True

def check_monotonicity_with_dampener(report):
    if not check_monotonicity(report):
        for i in range(len(report)):
            #print(report[:i] + report[i+1:])
            if check_monotonicity(report[:i] + report[i+1:]):
                return True
        return False
    return True


def ex1(file):
    reports = read_file(file)
    return sum((1 for report in reports if check_monotonicity(report)))

def ex2(file):
    reports = read_file(file)
    return sum((1 for report in reports if check_monotonicity_with_dampener(report)))

if __name__ == "__main__":
    print(ex1("day2/input.txt"))
    print(ex2("day2/input.txt"))

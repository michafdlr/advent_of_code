from utils import read_file

def check_value(values, test_value):
    if len(values) == 1:
        return values[0] == test_value
    return (check_value([values[0] + values[1]] + values[2:], test_value) or check_value([values[0] * values[1]] + values[2:], test_value))

def ex1():
    test_values, values = read_file("day7/input.txt")
    calibration_result = 0
    for i in range(len(values)):
        if check_value(values[i], test_values[i]):
            calibration_result += test_values[i]
    return calibration_result

if __name__ == "__main__":
    print(ex1())

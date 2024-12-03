from utils import read_file
import re

def mul(match):
    match = match.strip("mul(").rstrip(")").split(",")
    return int(match[0]) * int(match[1])

def ex1():
    pattern = "mul[(][0-9]{1,3},[0-9]{1,3}[)]"
    string = read_file("day3/input.txt")
    matches = re.findall(pattern, string)
    return sum((mul(match) for match in matches))

def ex2():
    pattern = "mul[(][0-9]{1,3},[0-9]{1,3}[)]"
    dont_pattern = "don't[(][)]"
    do_pattern = "do[(][)]"
    string = read_file("day3/input.txt").strip()
    total = 0
    while string:
        dont = re.search(dont_pattern, string)
        if not dont:
            matches = re.findall(pattern, string[:dont_start])
            total += sum((mul(match) for match in matches))
            break
        dont_start, dont_end = dont.start(), dont.end()

        matches = re.findall(pattern, string[:dont_start])
        total += sum((mul(match) for match in matches))

        string = string[dont_end:]
        do = re.search(do_pattern, string)
        if not do:
            break
        do_end = do.end()
        string = string[do_end:]
    return total

if __name__ == "__main__":
    print(ex1())
    print(ex2())

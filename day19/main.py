def read_file(filename):
    stripes = []
    designs = []
    with open(filename, "r") as f:
        file = f.read().split("\n\n")
    stripes = file[0].split(", ")
    designs = file[1].splitlines()
    return stripes, designs

def can_create_target(strings, target):
    memo = {}

    def can_construct(substring):
        if substring == "":
            return True
        if substring in memo:
            return memo[substring]
        for string in strings:
            if substring.startswith(string):
                suffix = substring[len(string):]
                if can_construct(suffix):
                    memo[substring] = True
                    return True
        memo[substring] = False
        return False

    return can_construct(target)


def ex1():
    stripes, designs = read_file("day19/input.txt")
    possible = 0
    for design in designs:
        if can_create_target(stripes, design):
            possible += 1
    return possible


#################### PART 2 ############################

def count_ways(strings, target):
    memo = {}

    def count(substring):
        if substring == "":
            return 1
        if substring in memo:
            return memo[substring]
        total_count = 0
        for word in strings:
            if substring.startswith(word):
                suffix = substring[len(word):]
                total_count += count(suffix)
        memo[substring] = total_count
        return total_count

    return count(target)

def ex2():
    stripes, designs = read_file("day19/input.txt")
    total = 0
    for design in designs:
        total += count_ways(stripes, design)
    return total

if __name__ == "__main__":
    print(ex1())
    print(ex2())

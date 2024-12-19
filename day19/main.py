def read_file(filename):
    stripes = []
    designs = []
    with open(filename, "r") as f:
        file = f.read().split("\n\n")
    stripes = file[0].split(", ")
    designs = file[1].splitlines()
    return stripes, designs

def check_substring(substring, stripes, memo):
    if substring == "":
        return True
    if substring in memo:
        return memo[substring]
    for stripe in stripes:
        if substring.startswith(stripe):
            suffix = substring[len(stripe):]
            if check_substring(suffix, stripes, memo):
                memo[substring] = True
                return True
    memo[substring] = False
    return False

def ex1():
    stripes, designs = read_file("day19/input.txt")
    return sum(check_substring(design, stripes, {}) for design in designs)


#################### PART 2 ############################

def count_possible_ways(substring, stripes, memo):
    if substring == "":
        return 1
    if substring in memo:
        return memo[substring]
    count = 0
    for stripe in stripes:
        if substring.startswith(stripe):
            suffix = substring[len(stripe):]
            count += count_possible_ways(suffix, stripes, memo)
    memo[substring] = count
    return count

def ex2():
    stripes, designs = read_file("day19/input.txt")
    return sum(count_possible_ways(design, stripes, {}) for design in designs)

if __name__ == "__main__":
    print(ex1())
    print(ex2())

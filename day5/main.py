from utils import read_file

def check_order(order, rules):
    for i in range(len(order)-1):
            for j in range(i+1, len(order)):
                if order[j] in rules and order[i] in rules[order[j]]:
                    return False
    return True

def fix_order(order, rules):
    for i in range(len(order)-1):
            for j in range(i+1, len(order)):
                if order[j] in rules and order[i] in rules[order[j]]:
                    order[j], order[i] = order[i], order[j]
    return order

def ex1():
    rules, orderings = read_file("day5/input.txt")
    total = 0
    for ordering in orderings:
        ordering = list(map(int, ordering.split(",")))
        if check_order(ordering, rules):
            total += ordering[len(ordering)//2]
    return total

def ex2():
    rules, orderings = read_file("day5/input.txt")
    total = 0
    for ordering in orderings:
        ordering = list(map(int, ordering.split(",")))
        if not check_order(ordering, rules):
            while not check_order(ordering, rules):
                ordering = fix_order(ordering, rules)
            total += ordering[len(ordering)//2]
    return total


if __name__ == "__main__":
    print(ex2())



def read_file(filename):
    with open(filename, "r") as f:
        numbers = list(map(int,f.read().splitlines()))
    return numbers

MODULO = 16777216

def mix(old, new):
    return old ^ new

def prune(old):
    return old % MODULO

def step1(num):
    new = num * 64
    return prune(mix(num, new))

def step2(num):
    return prune(mix(num, num // 32))

def step3(num):
    return prune(mix(num, num * 2048))

def build_secret_number(num):
    new_num = step1(num)
    new_num = step2(new_num)
    return step3(new_num)



def ex1():
    numbers = read_file("day22/input.txt")
    new_numbers = []
    for num in numbers:
        for _ in range(2000):
            num = build_secret_number(num)
        new_numbers.append(num)
    return sum(new_numbers)

if __name__ == "__main__":
    print(ex1())

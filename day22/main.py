import time

def read_file(filename):
    with open(filename, "r") as f:
        numbers = list(map(int,f.read().splitlines()))
    return numbers


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Time needed for function {func.__name__}: {end-start:.2f} sec\n")
        return result
    return wrapper

# Note:
# 64 = 2**6
# 32 = 2**5
# 2048 = 2**11
# 16777216 = 2**24

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
    return step3(step2(step1(num)))


@timer
def ex1():
    numbers = read_file("day22/input.txt")
    total = 0
    for num in numbers:
        for _ in range(2000):
            num = build_secret_number(num)
        total += num
    return total


################### PART 2 ###################################

def get_last_digit(num):
    return int(str(num)[-1])

@timer
def ex2():
    numbers = read_file("day22/input.txt")
    sequence_cache = {}
    for num in numbers:
        sequences = set()
        digits = [get_last_digit(num)]
        differences = []
        for i in range(2000):
            num = build_secret_number(num)
            digit = get_last_digit(num)
            if i == 0:
                digits.append(digit)
                differences.append(digits[1] - digits[0])
            else:
                digits[0], digits[1] = digits[1], digit
                differences.append(digits[1] - digits[0])
            if len(differences) == 4:
                seq = tuple(differences)
                if seq not in sequences:
                    sequences.add(seq)
                    if seq not in sequence_cache:
                        sequence_cache[seq] = digit
                    else:
                        sequence_cache[seq] += digit
                differences = differences[1:]
    return max(sequence_cache.values())

if __name__ == "__main__":
    print(f"Solution 1: {ex1()}\n", end=f"{20*'-'}\n")
    print(f"Solution 2: {ex2()}")

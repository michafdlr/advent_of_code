

def read_file(filename):
    with open(filename, "r") as f:
        numbers = list(map(int,f.read().splitlines()))
    return numbers

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

"""
def prune(value):
    return value & 0x00FFFFFF

def step1(num):
    new = num << 6
    return prune(num ^ new)

def step2(num):
    return prune(num ^ (num >> 5))

def step3(num):
    new = num << 11
    return prune(num ^ new)
"""

def build_secret_number(num):
    return step3(step2(step1(num)))



def ex1():
    numbers = read_file("day22/input.txt")
    final_cache = {}
    new_numbers = []
    for num in numbers:
        if num not in final_cache:
            temp = num
            for _ in range(2000):
                temp = build_secret_number(temp)
            final_cache[num] = temp
        new_numbers.append(final_cache[num])
    return sum(new_numbers)


################### PART 2 ###################################

def get_last_digit(num):
    return int(str(num)[-1])


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
    print(ex1())
    print(ex2())

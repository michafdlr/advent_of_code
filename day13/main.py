from fractions import Fraction

def read_file(filename):
    machines = []
    with open(filename, "r") as f:
        file = f.read()
        file.rstrip()
        lines = file.split("\n\n")
    for line in lines:
        machine = {}
        line = line.rstrip("\n")
        line = line.split("\n")
        for i in range(len(line)):
            if i % 3 == 0:
                l = line[i].split(": ")[1]
                l = l.split(", ")
                l[0], l[1] = int(l[0].strip("X+")), int(l[1].strip("Y+"))
                machine["A"] = l
            elif i % 3 == 1:
                l = line[i].split(": ")[1]
                l = l.split(", ")
                l[0], l[1] = int(l[0].strip("X+")), int(l[1].strip("Y+"))
                machine["B"] = l
            else:
                l = line[i].split(": ")[1]
                l = l.split(", ")
                l[0], l[1] = int(l[0].strip("X=")) + 10000000000000, int(l[1].strip("Y=")) + 10000000000000
                machine["Prize"] = l
        machines.append(machine)
    return machines


def get_pushes_algebraic(machine):
    x_price, y_price = machine["Prize"]
    a_x, a_y = machine["A"]
    b_x, b_y = machine["B"]
    b_pushes = Fraction(y_price*a_x - x_price*a_y, b_y*a_x - b_x*a_y)
    a_pushes = Fraction(x_price - b_pushes*b_x, a_x)
    return a_pushes, b_pushes

def ex2():
    machines = read_file("day13/input.txt")
    tokens = 0
    for machine in machines:
        a_pushes, b_pushes = get_pushes_algebraic(machine)
        if a_pushes - int(a_pushes) == 0 and b_pushes - int(b_pushes) == 0:
            tokens += a_pushes * 3 + b_pushes
    return tokens


if __name__ == "__main__":
    print(ex2())

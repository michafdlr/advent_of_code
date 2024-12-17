def read_file(filename):
    registers = {}
    program = []
    with open(filename, "r") as f:
        file = f.read().rstrip("\n").split("\n\n")
    program = file[-1].lstrip("Program: ").split(",")
    registers["A"] = int(file[0].splitlines()[0].strip("Register A: "))
    registers["B"], registers["C"] = 0, 0
    return program, registers

program, registers = read_file("day17/input.txt")

combo_operands = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: registers["A"],
    5: registers["B"],
    6: registers["C"]
}

def adv(combo_operands, operand):
    denominator = 2**combo_operands[operand]
    combo_operands[4] = combo_operands[4] // denominator
    return

def bxl(combo_operands, operand):
    combo_operands[5] = combo_operands[5] ^ operand
    return

def bst(combo_operands, operand):
    combo_operands[5] = combo_operands[operand] % 8
    return

def jnz(combo_operands, operand):
    if combo_operands[4] == 0:
        return
    return operand

def bxc(combo_operands, operand):
    combo_operands[5] = combo_operands[5] ^ combo_operands[6]

def out(combo_operands, operand):
    return combo_operands[operand] % 8

def bdv(combo_operands, operand):
    denominator = 2**combo_operands[operand]
    combo_operands[5] = combo_operands[4] // denominator
    return

def cdv(combo_operands, operand):
    denominator = 2**combo_operands[operand]
    combo_operands[6] = combo_operands[4] // denominator
    return

opcode_to_instruction = {
    "0": adv,
    "1": bxl,
    "2": bst,
    "3": jnz,
    "4": bxc,
    "5": out,
    "6": bdv,
    "7": cdv
}

def ex1(combo_operands):

    output = []
    i_pointer = 0
    steps = 1
    while i_pointer < len(program):
        opcode, operand = program[i_pointer:i_pointer+2]
        operand = int(operand)
        if opcode not in ["3", "5"]:
            opcode_to_instruction[opcode](combo_operands, operand)
            i_pointer += 2
        elif opcode == "5":
            output.append(str(opcode_to_instruction[opcode](combo_operands, operand)))
            #print(steps)
            i_pointer += 2
        elif opcode == "3":
            if opcode_to_instruction[opcode](combo_operands, operand) is not None:
                i_pointer = opcode_to_instruction[opcode](combo_operands, operand)
            else:
                i_pointer += 2
        steps += 1
    return ",".join(output)

def ex2():
    values = [0]
    for i in range(16):
        new_values = []
        for val in values:
            for a in range(8):
                new_A = val * 8 + a
                combo_operands[4] = new_A
                new_P = ex1(combo_operands)
                if new_P == ",".join(program)[-2 * i - 1:]:
                    new_values.append(new_A)
                    if i == 15:
                        return new_A
        values = new_values

if __name__ == "__main__":
    print(ex1(combo_operands))
    print(ex2())

def read_file(filename):
    registers = {}
    program = []
    with open(filename, "r") as f:
        file = f.read().rstrip("\n").split("\n\n")
    program = file[-1].lstrip("Program: ").split(",")
    registers["A"] = int(file[0].splitlines()[0].strip("Register A: "))
    registers["B"], registers["C"] = 0, 0
    return program, registers

program, registers = read_file("day17/testinput.txt")

combo_operands = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: registers["A"],
    5: registers["B"],
    6: registers["C"]
}

def adv(operand):
    denominator = 2**combo_operands[operand]
    combo_operands[4] = combo_operands[4] // denominator
    return

def bxl(operand):
    combo_operands[5] = combo_operands[5] ^ operand
    return

def bst(operand):
    combo_operands[5] = combo_operands[operand] % 8
    return

def jnz(operand):
    if combo_operands[4] == 0:
        return
    return operand

def bxc(operand):
    combo_operands[5] = combo_operands[5] ^ combo_operands[6]

def out(operand):
    return combo_operands[operand] % 8

def bdv(operand):
    denominator = 2**combo_operands[operand]
    combo_operands[5] = combo_operands[4] // denominator
    return

def cdv(operand):
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

def ex1():
    print(program, registers)
    output = []
    i_pointer = 0
    while i_pointer < len(program):
        opcode, operand = program[i_pointer:i_pointer+2]
        operand = int(operand)
        if opcode not in ["3", "5"]:
            opcode_to_instruction[opcode](operand)
            i_pointer += 2
        elif opcode == "5":
            output.append(str(opcode_to_instruction[opcode](operand)))
            i_pointer += 2
        elif opcode == "3":
            if opcode_to_instruction[opcode](operand) is not None:
                i_pointer = opcode_to_instruction[opcode](operand)
            else:
                i_pointer += 2
    return ",".join(output)

if __name__ == "__main__":
    print(ex1())

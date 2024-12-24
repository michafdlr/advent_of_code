import time
from typing import NamedTuple

def read_file(filename):
    with open(filename, "r") as f:
        parts = f.read().rstrip("\n").split("\n\n")
    wires = parts[0].splitlines()
    connections = parts[1].splitlines()
    wire_values = {}
    for wire in wires:
        wire = wire.split(": ")
        wire_values[wire[0]] = int(wire[1])
    gates = []
    for conn in connections:
        conn = conn.split(" ")
        gates.append((conn[0], conn[1], conn[2], conn[-1]))
    return wire_values, gates


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Time needed for function {func.__name__}: {end-start:.2f} sec\n")
        return result
    return wrapper


@timer
def ex1():
    wire_values, gates = read_file("day24/input.txt")
    while gates:
        for (wire1, gate, wire2, output) in gates:
            if wire1 not in wire_values or wire2 not in wire_values:
                continue
            else:
                if gate == "AND":
                    wire_values[output] = wire_values[wire1] & wire_values[wire2]
                if gate == "OR":
                    wire_values[output] = wire_values[wire1] | wire_values[wire2]
                if gate == "XOR":
                    wire_values[output] = wire_values[wire1] ^ wire_values[wire2]
                gates.remove((wire1, gate, wire2, output))
    binary = ""
    for wire, value in sorted(wire_values.items()):
        if wire.startswith("z"):
            binary = str(value) + binary
    return int(binary, base=2)


#################### PART 2 ###########################


## ADAPTED FROM https://github.com/janek37/advent-of-code/blob/main/2024/day24.py doc-strings added

class GateExpression(NamedTuple):
    label: str
    position: int


class Mismatch(NamedTuple):
    expr1: "GateExpression | Mismatch"
    expr2: "GateExpression | Mismatch"
    gate: str
    position: int


def find_swaps(gates):
    """
    Finds and yields swaps in the gates until no more swaps are found.

    Args:
        gates (list): A list of tuples representing the gates. Each tuple contains (wire1, gate, wire2, output).

    Yields:
        tuple: A tuple containing the outputs to be swapped.
    """
    while True:
        swap = find_swap(gates)
        if swap:
            yield swap
            swap_outputs(swap[0], swap[1], gates)
        else:
            break


def find_swap(gates):
    """
    Finds a single swap in the gates.

    Args:
        gates (list): A list of tuples representing the gates. Each tuple contains (wire1, gate, wire2, output).

    Returns:
        tuple: A tuple containing the outputs to be swapped, or None if no swap is found.
    """
    output_to_gates_dict = {output: (wire1, gate, wire2) for wire1, gate, wire2, output in gates}
    expressions = {get_expression(output, output_to_gates_dict): output for output in output_to_gates_dict}
    for expr, output in expressions.items():
        expr = get_expression(output, output_to_gates_dict)
        if expr.position == -1 and output.startswith("z"):
            expr1, expr2, gate, _ = expr
            position = int(output[1:])
            if gate == "XOR":
                wire1, _, wire2 = output_to_gates_dict[output]
                other_wire = {expr: wire for expr, wire in zip((expr1, expr2), (wire2, wire1))}
                if GateExpression("Carry", position) in (expr1, expr2):
                    return (
                        other_wire[GateExpression("Carry", position)],
                        expressions[GateExpression("Xor", position)],
                    )
                if GateExpression("Xor", position) in (expr1, expr2):
                    return (
                        other_wire[GateExpression("Xor", position)],
                        expressions[GateExpression("Carry", position)],
                    )
        elif expr.position < 0:
            continue
        elif expr.label == "Digit" and output != f"z{expr.position:02d}":
            return output, f"z{expr.position:02d}"


def get_expression(output, output_to_gates_dict):
    """
    Gets the expression for a given output.

    Args:
        output (str): The output wire name.
        output_to_gates_dict (dict): A dictionary mapping output wire names to their gate tuples.

    Returns:
        GateExpression or Mismatch: The expression for the given output.
    """
    if output[0] in "xy":
        return GateExpression(output[0], int(output[1:]))
    wire1, gate, wire2 = output_to_gates_dict[output]
    expr1 = get_expression(wire1, output_to_gates_dict)
    expr2 = get_expression(wire2, output_to_gates_dict)
    if isinstance(expr1, GateExpression) and isinstance(expr2, GateExpression) and expr1.position == expr2.position:
        labels = {expr1.label, expr2.label}
        if labels == {"x", "y"}:
            if gate == "XOR":
                return GateExpression("Xor" if expr1.position > 0 else "Digit", expr1.position)
            elif gate == "AND":
                if expr1.position == 0:
                    return GateExpression("Carry", 1)
                else:
                    return GateExpression("And", expr1.position)
        if labels == {"Carry", "Xor"} and gate in ("AND", "XOR"):
            return GateExpression("Partial" if gate == "AND" else "Digit", expr1.position)
        if labels == {"Partial", "And"} and gate == "OR":
            return GateExpression("Carry", expr1.position + 1)
    if expr1.position < 0 or expr2.position < 0:
        return Mismatch(expr1, expr2, gate, -2)
    return Mismatch(expr1, expr2, gate, -1)


def swap_outputs(output1, output2, gates):
    """
    Swaps the outputs in the gates.

    Args:
        output1 (str): The first output wire name.
        output2 (str): The second output wire name.
        gates (list): A list of tuples representing the gates. Each tuple contains (wire1, gate, wire2, output).
    """
    for i, (wire1, gate, wire2, output) in enumerate(gates):
        if output == output1:
            new_output = output2
        elif output == output2:
            new_output = output1
        else:
            new_output = output
        gates[i] = (wire1, gate, wire2, new_output)

@timer
def ex2():
    _, gates = read_file("day24/input.txt")
    swap1, swap2, swap3, swap4 = find_swaps(gates)
    return ",".join(sorted(swap1 + swap2 + swap3 + swap4))


if __name__ == '__main__':
    print(f"Solution 1: {ex1()}\n", end=f"{20*'-'}\n")
    print(f"Solution 2: {ex2()}")

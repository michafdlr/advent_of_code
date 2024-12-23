import time
import networkx as nx
from itertools import combinations


def read_file(filename):
    with open(filename, "r") as f:
        connections = f.read().splitlines()
    connection_dict = {}
    for conn in connections:
        conn = conn.split("-")
        if conn[0] not in connection_dict:
            connection_dict[conn[0]] = [conn[1]]
        else:
            connection_dict[conn[0]].append(conn[1])
    return connection_dict


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Time needed for function {func.__name__}: {end-start:.2f} sec\n")
        return result
    return wrapper

def check_for_t(comb):
    for el in comb:
        if el.startswith("t"):
            return True
    return False

@timer
def ex1():
    connections = read_file("day23/input.txt")
    graph = nx.from_dict_of_lists(connections)
    cliques = nx.find_cliques(graph)
    clique_set = set()
    for clique in cliques:
        if len(clique) >= 3:
            for comb in combinations(clique, r=3):
                if check_for_t(comb):
                    clique_set.add(tuple(sorted(comb)))
    return len(clique_set)

@timer
def ex2():
    connections = read_file("day23/input.txt")
    graph = nx.from_dict_of_lists(connections)
    return ",".join(sorted(max(nx.find_cliques(graph), key = len, default=[])))

if __name__ == "__main__":
    print(f"Solution 1: {ex1()}\n", end=f"{20*'-'}\n")
    print(f"Solution 2: {ex2()}")

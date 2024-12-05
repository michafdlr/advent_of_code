def read_file(file):
    rules_input = []
    orderings = []
    with open(file, "r") as f:
        lines = f.read().split("\n\n")
    rules_input = lines[0].split("\n")
    orderings = lines[1].split("\n")

    rules = {}
    for rule in rules_input:
        rule = list(map(int, rule.split("|")))
        if rule[0] in rules:
            rules[rule[0]].append(rule[1])
        else:
            rules[rule[0]] = [rule[1]]
    return rules, orderings[:-1]

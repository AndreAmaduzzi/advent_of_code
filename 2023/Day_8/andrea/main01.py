"""
8th December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")

    steps = lines[0]
    aux_rules = lines[1:]
    aux_rules.pop(0)

    rules = []

    for x in aux_rules:
        rule = []
        rule.append(x[:3])
        rule.append(x[7:10])
        rule.append(x[-4:-1])
        rules.append(rule)

    pos = "AAA"
    count = 0
    id_step = 0
    act_step = steps[id_step]
    num_step = len(steps)

    while pos != "ZZZ":
        for rule in rules:
            if rule[0] == pos:
                count += 1
                if act_step == "L":
                    pos = rule[1]
                else:
                    pos = rule[2]
                id_step += 1
                if id_step == num_step:
                    id_step = 0
                act_step = steps[id_step]
                break

    print("Soluzione:")
    print(count)


if __name__ == "__main__":
    main()

"""
8th December, 2023
"""
from itertools import cycle
import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def main():
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")

    steps = lines[0]
    aux_rules = lines[1:]
    aux_rules.pop(0)

    rules = []

    rules = {rule[0:3]: {"L": rule[7:10], "R": rule[12:15]} for rule in aux_rules}

    positions = [rule for rule in rules if str(rule).endswith("A")]
    totals = [0] * len(positions)

    for i, pos in enumerate(positions):
        c = cycle(steps)
        while not pos.endswith("Z"):
            totals[i] += 1
            pos = rules[pos][next(c)]

    sol_t = 1
    for x in totals:
        sol_t = lcm(sol_t, x)

    print("Soluzione:")
    print(sol_t)


if __name__ == "__main__":
    main()

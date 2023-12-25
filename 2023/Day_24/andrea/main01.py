"""
24th December, 2023
"""

import re
from itertools import combinations

import numpy as np
from z3 import Int, IntVector, Solver

def main():
    with open('input.txt', 'r') as f:
        ls = f.read().strip().split("\n")

    ns = [list(map(int, re.findall("-?\d+", x))) for x in ls]

    # Part 1
    lo = 200000000000000
    hi = 400000000000000

    res = 0
    for n1, n2 in combinations(ns, 2):
        p1, p2, _, dp1, dp2, _ = n1
        q1, q2, _, dq1, dq2, _ = n2
        sp = dp2 / dp1
        sq = dq2 / dq1
        if sp == sq:
            continue
        x, y = np.linalg.solve([[-sp, 1], [-sq, 1]], [p2 - sp * p1, q2 - sq * q1])
        if (x - p1) / dp1 < 0 or (x - q1) / dq1 < 0:
            continue
        if lo <= x <= hi and lo <= y <= hi:
            res += 1

    print('Soluzione:')
    print(res)

if __name__ == '__main__':
    main()
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
    
    # Part 2
    q1, q2, q3, dq1, dq2, dq3 = IntVector("sol", 6)
    ts = IntVector("t", len(ns))
    s = Solver()

    for t, (p1, p2, p3, dp1, dp2, dp3) in zip(ts, ns):
        s.add(q1 + t * dq1 == p1 + t * dp1)
        s.add(q2 + t * dq2 == p2 + t * dp2)
        s.add(q3 + t * dq3 == p3 + t * dp3)

    s.check()
    m = s.model()

    print('Soluzione:')
    print(sum(m[v].as_long() for v in (q1, q2, q3)))


if __name__ == '__main__':
    main()
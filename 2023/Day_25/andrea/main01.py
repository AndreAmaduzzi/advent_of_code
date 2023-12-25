"""
24th December, 2023
"""

import math, random

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    V = set()
    E = set()

    for line in lines:
        v, *ws = line.replace(':',' ').split()
        V |= {v, *ws}
        E |= {(v,w) for w in ws}

    ss = lambda v: next(s for s in subsets if v in s)

    while True:
        subsets = [{v} for v in V]
        
        while len(subsets) > 2:
            s1, s2 = map(ss, random.choice([*E]))
            if s1 != s2:
                s1 |= s2; 
                subsets.remove(s2)
        if sum(ss(u) != ss(v) for u,v in E) < 4:
            break

    print('Soluzione:')
    print(math.prod(map(len, subsets)))

if __name__ == '__main__':
    main()


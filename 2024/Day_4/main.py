"""
4st December, 2024
"""

import sys
import re
from collections import defaultdict, Counter

def pr(s):
    print(s)


sys.setrecursionlimit(10**6)

def main():
    p1 = 0
    p2 = 0
    with open('input.txt') as f:
         data = f.read().strip()

    G = data.split('\n')
    R = len(G)
    C = len(G[0])
    for r in range(R):
        for c in range(C):
            if c+3<C and G[r][c]=='X' and G[r][c+1]=='M' and G[r][c+2]=='A' and G[r][c+3]=='S':
                p1 += 1
            if r+3<R and G[r][c]=='X' and G[r+1][c]=='M' and G[r+2][c]=='A' and G[r+3][c]=='S':
                p1 += 1
            if r+3<R and c+3<C and G[r][c]=='X' and G[r+1][c+1]=='M' and G[r+2][c+2]=='A' and G[r+3][c+3]=='S':
                p1 += 1
            if c+3<C and G[r][c]=='S' and G[r][c+1]=='A' and G[r][c+2]=='M' and G[r][c+3]=='X':
                p1 += 1
            if r+3<R and G[r][c]=='S' and G[r+1][c]=='A' and G[r+2][c]=='M' and G[r+3][c]=='X':
                p1 += 1
            if r+3<R and c+3<C and G[r][c]=='S' and G[r+1][c+1]=='A' and G[r+2][c+2]=='M' and G[r+3][c+3]=='X':
                p1 += 1
            if r-3>=0 and c+3<C and G[r][c]=='S' and G[r-1][c+1]=='A' and G[r-2][c+2]=='M' and G[r-3][c+3]=='X':
                p1 += 1
            if r-3>=0 and c+3<C and G[r][c]=='X' and G[r-1][c+1]=='M' and G[r-2][c+2]=='A' and G[r-3][c+3]=='S':
                p1 += 1

            if r+2<R and c+2<C and G[r][c]=='M' and G[r+1][c+1]=='A' and G[r+2][c+2]=='S' and G[r+2][c]=='M' and G[r][c+2]=='S':
                p2 += 1
            if r+2<R and c+2<C and G[r][c]=='M' and G[r+1][c+1]=='A' and G[r+2][c+2]=='S' and G[r+2][c]=='S' and G[r][c+2]=='M':
                p2 += 1
            if r+2<R and c+2<C and G[r][c]=='S' and G[r+1][c+1]=='A' and G[r+2][c+2]=='M' and G[r+2][c]=='M' and G[r][c+2]=='S':
                p2 += 1
            if r+2<R and c+2<C and G[r][c]=='S' and G[r+1][c+1]=='A' and G[r+2][c+2]=='M' and G[r+2][c]=='S' and G[r][c+2]=='M':
                p2 += 1

    pr(p1)
    pr(p2)

if __name__ == "__main__":
    main()

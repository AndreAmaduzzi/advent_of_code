"""
17th December, 2023
"""

from matplotlib.path import Path

MOVES = {
        ("R"): (0, 1),
        ("L"): (0, -1),
        ("U"): (-1, 0),
        ("D"): (1, 0),
        '0': (0,1), 
        '1': (1,0),
        '2': (0,-1),
        '3': (-1,0)
    }


def area(steps, pos=0, res=1):
    for (x,y), n in steps:
        pos += x*n
        res += y*n * pos + n/2

    return int(res)


def main():

    with open('input.txt', 'r') as f:
        lines = f.readlines()
   
    steps = []

    for line in lines:
        steps.append((line.split(' ')[2][7], int(line.split(' ')[2][2:7], 16))) 

    x = 0
    y = 0
    perimeter = 0
    area = 0
    for step in steps:
        direc, length = step
        dy, dx = MOVES[direc]
        dy, dx = dy*length, dx*length
        y, x = y+dy, x+dx
        perimeter+=length
        area+=x*dy

    sol = area+perimeter//2+1
    print('Soluzione:')
    print(sol)




if __name__ == "__main__":
    main()


    
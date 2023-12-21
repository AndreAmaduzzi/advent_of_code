"""
18th December, 2023
"""

MOVES = {
        ("R"): (0, 1),
        ("L"): (0, -1),
        ("U"): (-1, 0),
        ("D"): (1, 0),
    }

def main():

    with open('input.txt', 'r') as f:
        lines = f.readlines()
   
    steps = []

    for line in lines:
        steps.append((line.split(' ')[0], int(line.split(' ')[1]))) 

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

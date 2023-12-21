"""
17th December, 2023
"""

from matplotlib.path import Path

MOVES = {
        ("R"): (0, 1),
        ("L"): (0, -1),
        ("U"): (-1, 0),
        ("D"): (1, 0),
        '0': (1,0), 
        '1': (0,1),
        '2': (-1,0),
        '3': (0,-1)
    }


def area(steps, pos=0, res=1):
    for (x,y), n in steps:
        pos += x*n
        res += y*n * pos + n/2

    return int(res)


def main():

    with open('input.txt', 'r') as f:
        lines = f.readlines()
   
    directions = []
    steps = []
    dig_plan = []

    # for line in lines:
    #     directions.append(line.split(' ')[0])
    #     steps.append(int(line.split(' ')[1]))

    for line in lines:
        steps.append((line.split(' ')[0], int(line.split(' ')[1]))) 

    # print(directions)
    # print(steps)

    # sol = (area(MOVES[d], int(s)) for d,s,_ in steps)

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
    print('Inner area:',area)
    print('Perimeter: ',perimeter)
    print('Total area:',area+perimeter//2+1)



    # print(steps)

    # pos_x = 0
    # pos_y = 0
    # perimeter = 0
    # len_x = 0
    # len_y = 0

    # dig_plan.append([pos_x, pos_y])
    # for id, direction in enumerate(directions):
    #     for i in range(steps[id]):
    #         offset_x, offset_y = MOVES[direction]
    #         pos_x += offset_x
    #         pos_y += offset_y
    #         dig_plan.append([pos_x, pos_y])
    #         perimeter += 1
    #         if (pos_x > len_x):
    #             len_x = pos_x
    #         if (pos_y > len_y):
    #             len_y = pos_y

    # print("len_x = " + str(len_x))
    # print("len_y = " + str(len_y))
    # print(perimeter)

    # area = 0
    # p = Path(dig_plan)
    # for y in range(len_y):
    #     for x in range(len_x):
    #         if [x, y] in dig_plan:
    #             continue
    #         if p.contains_point((x, y)):
    #             area += 1
    
    # print(area)

    # print('Soluzione:')
    # print(perimeter+area)


if __name__ == "__main__":
    main()


    
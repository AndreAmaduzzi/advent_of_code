"""
10th December, 2023
"""
import math


def step_move(act_map, p_row, p_col, act_row, act_col):

    if (p_row != act_row - 1 or p_col != act_col) and (act_map[0][1] == '|' or act_map[0][1] == '7' or act_map[0][1] == 'F' or act_map[0][1] == 'S') and (act_map[1][1] != '7' and act_map[1][1] != 'F' and act_map[1][1] != '-'):
        return -1, 0
    elif (p_row != act_row or p_col != act_col - 1) and (act_map[1][0] == '-' or act_map[1][0] == 'F' or act_map[1][0] == 'L' or act_map[1][0] == 'S') and (act_map[1][1] != 'L' and act_map[1][1] != 'F' and act_map[1][1] != '|'):
        return 0, -1
    elif (p_row != act_row or p_col != act_col + 1) and (act_map[1][2] == '-' or act_map[1][2] == '7' or act_map[1][2] == 'J' or act_map[1][2] == 'S') and (act_map[1][1] != '7' and act_map[1][1] != 'J' and act_map[1][1] != '|'):
        return 0, 1
    elif (p_row != act_row + 1 or p_col != act_col) and (act_map[2][1] == '|' or act_map[2][1] == 'J' or act_map[2][1] == 'L' or act_map[2][1] == 'S') and (act_map[1][1] != 'L' and act_map[1][1] != 'J' and act_map[1][1] != '-'):
        return 1, 0
    else:
        print('Error!')


def main():
    with open("input.txt", "r") as f:
        map = f.readlines()

    n_row = len(map)
    n_col = len(map[0])

    map[n_row - 1] += '.'
    map.append(['.' for x in range(n_col)])

    found = False
    i = 0

    # Searching for starting point
    while not found:
        s_col = map[i].find('S')
        if s_col != -1:
            found = True
            s_row = i
        else:
            i += 1

    finish = False
    act_row = s_row
    act_col = s_col
    p_row = s_row
    p_col = s_col
    count = 0

    # Moving labirinth
    while not finish:

        act_map_move = [[map[act_row + i][act_col + j] for j in range(-1, 2)] for i in range(-1, 2)]

        step_row, step_col = step_move(act_map_move, p_row, p_col, act_row, act_col)

        p_row = act_row
        p_col = act_col
        act_row += step_row
        act_col += step_col
        count += 1

        if act_row == s_row and act_col == s_col:
            finish = True


    print("Soluzione:")
    print(math.trunc(count/2))


if __name__ == "__main__":
    main()

"""
10th December, 2023
"""

from matplotlib.path import Path

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

    file1 = open("output_maze.txt", "w")

    n_row = len(map)
    n_col = len(map[0])

    map[n_row - 1] += '.'
    map.append(['.' for x in range(n_col)])

    found = False
    i = 0

    maze = [['.' for j in range(len(map[0]))] for i in range(len(map))]

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
    area = 0

    maze_pipe = []
    maze_pipe.append([s_row, s_col])

    # Moving labirinth
    while not finish:

        act_map_move = [[map[act_row + i][act_col + j] for j in range(-1, 2)] for i in range(-1, 2)]

        step_row, step_col = step_move(act_map_move, p_row, p_col, act_row, act_col)
        
        area += act_row * step_col

        maze[act_row][act_col] = map[act_row][act_col]
        

        p_row = act_row
        p_col = act_col
        act_row += step_row
        act_col += step_col
        count += 1

        maze_pipe.append([act_row, act_col])

        if act_row == s_row and act_col == s_col:
            finish = True

    for idx, row in enumerate(maze):
        first_pipe = False
        last_pipe_id = len(row)
        for idy, ch in enumerate(row):
            if ch != '|' and ch != '-' and ch != 'J' and ch != 'F' and ch != 'L' and ch != '7' and ch != 'S':
                if not first_pipe:
                    maze[idx][idy] = '0'
            else:
                first_pipe = True
                last_pipe_id = idy
        
        for i in range(last_pipe_id + 1, len(row)):
            maze[idx][i] = '0'

    iteration_up = True

    while iteration_up:
        iteration_up = False
        for idx, row in enumerate(maze):
            for idy, ch in enumerate(row):
                if idx > 0 and idx < len(maze) - 1 and idy > 0 and idy < len(row) - 1:
                    if maze[idx][idy] == '0':
                        if maze[idx-1][idy] == '.':
                            maze[idx-1][idy] = '0'
                            iteration_up = True
                        elif maze[idx][idy-1] == '.':
                            maze[idx][idy-1] = '0'
                            iteration_up = True
                        elif maze[idx][idy+1] == '.':
                            maze[idx][idy+1] = '0'
                        elif maze[idx+1][idy] == '.':
                            maze[idx+1][idy] = '0'

    count_2 = 0

    for idx, row in enumerate(maze):
        for idy, ch in enumerate(row):
            if maze[idx][idy] == '.':
                count_2 += 1

    for line in maze:
        aux_line = ''
        for ch in line:
            aux_line += ch
        aux_line += '\n'
        file1.write(aux_line)

    file1.close()

    # Solution part 2 using path library
    ans_2 = 0
    p = Path(maze_pipe)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if [x, y] in maze_pipe:
                continue
            if p.contains_point((x, y)):
                ans_2 += 1


    print("Soluzione:")
    print("Part 2     :", area-count//2+1)
    print("Part 2     :", ans_2)

if __name__ == "__main__":
    main()

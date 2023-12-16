"""
14th December, 2023
"""

def tilt_platform_dir(platform, dir):
    tilted = False

    while not tilted:
        tilted = True
        for i, row in enumerate(platform):
            if i + dir[0] not in range(0, len(platform)):
                continue
            for j in range(len(row) - 1):
                if j + dir[1] not in range(0, len(platform[0])):
                    continue
                if platform[i][j] == 'O' and platform[i+dir[0]][j+dir[1]] == '.':
                    platform[i][j] = '.'
                    platform[i+dir[0]][j+dir[1]] = 'O'
                    tilted = False
    return platform

def tilt_cycle(platform):
    aux_platform = platform
    for i in ((-1,0), (-1, 0), (0, -1), (1, 0), (0, 1)):
        aux_platform = tilt_platform_dir(platform, i) 

    return aux_platform

def main():
    with open("test.txt", "r") as f:
        lines = f.readlines()

    platform = []

    for i, row in enumerate(lines):
        aux_row = []
        for j, ch in enumerate(row):
            aux_row.append(ch)
        platform.append(aux_row)

    # print(platform)

    seen = []
    i = 0
    goal = 1_000_000_000
    found_cycle = False
    while i < goal:
        i = i +1 
        platform = tilt_cycle(platform)
        # print(i)

        mnow = "".join(["".join(q) for q in platform])
        if(mnow in seen):
            first = seen.index(mnow)
            c = i-first
            f = (goal - first)%c+first
            platform = seen[f-1]
            break
        seen.append(mnow)
        # print(seen)
    
    print(platform)

    platform_end = []
    str = ''
    for item in platform:
        if item != 'O' and item != '.' and item != '#':
            platform_end.append(str)
            str = ''
        else:
            str += item

    print(platform_end)
    
    sum = 0
    for row_i in range(0, len(platform_end[0])-1):
        count_rocks = 0
        for row_j in range(0, len(platform_end)):
            if platform_end[row_j][row_i] == 'O':
                count_rocks += 1
            if count_rocks > 0:
                sum += count_rocks
                

    print('Soluzione:')
    print(sum)


if __name__ == "__main__":
    main()
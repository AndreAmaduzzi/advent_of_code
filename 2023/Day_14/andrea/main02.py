"""
14th December, 2023
"""

# @functools.lru_cache(maxsize=None)
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

# @functools.lru_cache(maxsize=None)
def tilt_cycle(platform):
    aux_platform = platform
    for i in ((-1,0), (-1, 0), (0, -1), (1, 0), (0, 1)):
        aux_platform = tilt_platform_dir(platform, i) 

    return aux_platform

def load(platform):
    return sum(100 - z.real for z in platform)

def main():
    with open("test.txt", "r") as f:
        lines = f.readlines()

    platform =  []

    for i, row in enumerate(lines):
        aux_row = []
        for j, ch in enumerate(row):
            aux_row.append(ch)
        platform.append(aux_row)

    seen = {}
    count = 0
    cycle = 0
    goal = 1_000_000_000
    found_cycle = False
    while cycle < goal:

        # print('Seen platform')
        # for i_plat in seen:
        #     for line in i_plat:
        #         print(line[:-1])
        #     print()

        # print()

        platform = tilt_cycle(platform)
        # count += 1
        # print()
        # print('New platform')
        # for line in platform:
        #     print(line[:-1])

        # print()

        # print(platform in seen)

        # if platform in seen:
        #     start = seen.index(platform)
        #     break
        # seen.append(platform)

        if not found_cycle and (found_cycle := platform in seen):
            cycle_length = cycle - seen[platform]
            cycle += cycle_length * ((goal - cycle) // cycle_length)
        else:
            seen[platform] = cycle

    
    sum = 0
    for row_i in range(0, len(platform[0])-1):  # loop over chars
        count_rocks = 0
        for row_j in range(0, len(platform)):   # loop over rows
            if platform[row_j][row_i] == 'O':
                count_rocks += 1
            if count_rocks > 0:
                sum += count_rocks
                
    print(count)

    print('Soluzione:')
    print(sum)
    print(load(seen[(1000000000 - i) % (start - i) + i - 1]))


if __name__ == "__main__":
    main()
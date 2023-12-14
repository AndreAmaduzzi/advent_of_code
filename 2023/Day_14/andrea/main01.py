"""
14th December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    platform =  []

    for i, row in enumerate(lines):
        aux_row = []
        for j, ch in enumerate(row):
            aux_row.append(ch)
        platform.append(aux_row)

    tilted = False

    while not tilted:
        tilted = True
        for i, row in enumerate(lines):
            for j, ch in enumerate(row):
                if platform[i][j] == 'O' and platform[i-1][j] == '.' and i>0:
                    platform[i][j] = '.'
                    platform[i-1][j] = 'O'
                    tilted = False

    sum = 0
    for row_i in range(0, len(platform[0])-1):  # loop over chars
        count_rocks = 0
        for row_j in range(0, len(platform)):   # loop over rows
            if platform[row_j][row_i] == 'O':
                count_rocks += 1
            if count_rocks > 0:
                sum += count_rocks
                

    print('Soluzione:')
    print(sum)


if __name__ == "__main__":
    main()
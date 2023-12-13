"""
3rd December, 2023
"""

def check_symbol(lines, r, c, n_row, n_col):
    
    if (((lines[r-1][c-1].isdecimal() == False and lines[r-1][c-1] != '.') and r >= 1 and c >= 1) or
        ((lines[r-1][c].isdecimal() == False and lines[r-1][c] != '.') and r >= 1) or
        ((lines[r-1][c+1].isdecimal() == False and lines[r-1][c+1] != '.') and r >= 1 and c < n_col - 1) or
        ((lines[r][c-1].isdecimal() == False and lines[r][c-1] != '.') and c >= 1) or
        ((lines[r][c+1].isdecimal() == False and lines[r][c+1] != '.') and c < n_col - 1)):
        return True
    elif r < n_row - 1:
        if (((not lines[r+1][c-1].isdecimal() and lines[r+1][c-1] != '.') and r < n_row and c >= 1) or
            ((not lines[r+1][c].isdecimal() and lines[r+1][c] != '.') and r < n_row) or
            ((not lines[r+1][c+1].isdecimal() and lines[r+1][c+1] != '.') and r < n_row and c < n_col - 1)):
            return True
        else:
            return False
    else:
        return False


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    n_row = len(lines)
    n_column = len(lines[0]) - 1
    sum = 0
    count = 0

    for idx_r, line in enumerate(lines):
        act_num = ''
        is_num = False
        has_symbol = 0
        for idx_c, ch in enumerate(line):
            if ch.isdecimal():
                is_num = True
                act_num += ch
                if check_symbol(lines, idx_r, idx_c, n_row, n_column):
                    has_symbol += 1
            else:
                if len(act_num) > 0 and is_num and has_symbol >= 1:
                    sum += int(act_num)
                    count += 1
                act_num = ''
                is_num = False
                has_symbol = 0

    print('Soluzione:')
    print(sum)
    print(count)

if __name__ == "__main__":
    main()

"""
3rd December, 2023
"""
from collections import defaultdict


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    n_row = len(lines)
    n_column = len(lines[0]) - 1
    sum = 0
    count = 0
    nums = defaultdict(list)

    for idx_r, line in enumerate(lines):
        gears = set() # positions of '*' characters next to the current number
        act_num = 0
        is_num = False
        has_symbol = 0
        for idx_c, ch in enumerate(line):
            if ch.isdecimal():
                act_num = act_num*10+int(lines[idx_r][idx_c])
                for rr in [-1,0,1]:
                    for cc in [-1,0,1]:
                        if 0 <= idx_r+rr < n_row and 0 <= idx_c+cc < n_column:
                            ch = lines[idx_r+rr][idx_c+cc]
                        if not ch.isdigit() and ch != '.':
                            is_num = True
                            has_symbol = True
                        if ch=='*':
                            gears.add((idx_r+rr, idx_c+cc))
            else:
                for gear in gears:
                    nums[gear].append(act_num)
                if is_num and has_symbol >= 1:
                    sum += int(act_num)
                    count += 1
                act_num = 0
                is_num = False
                has_symbol = 0
                gears = set()

    sum_02 = 0
    for k,v in nums.items():
        if len(v)==2:
            sum_02 += v[0]*v[1]
    print('Soluzione:')
    print(sum_02)

if __name__ == "__main__":
    main()

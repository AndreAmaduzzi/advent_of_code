'''
4st December, 2022
'''


def calc_range(str) -> list:
    num1, num2 = str.split('-')
    return [int(num1), int(num2)]

def check_range(range1, range2) -> bool:
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    elif range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    else:
        return False

def check_range_v2(range1, range2) -> bool:
    if (range1[0] >= range2[0] and range1[0] <= range2[1]) or (range1[1] >= range2[0] and range1[1] <= range2[1]):
        return True
    elif check_range(range1,range2):
        return True
    else:
        return False



def main():

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    sum_part1 = 0
    sum_part2 = 0
    for line in lines:
        elf1, elf2 = line.split(',')
        if elf2[-1] == '\n':
            elf2 = elf2[:-1]
        elf1 = calc_range(elf1)
        elf2 = calc_range(elf2)

        if check_range(elf1, elf2):
            sum_part1 += 1

        if check_range_v2(elf1, elf2):
            sum_part2 += 1


    print(sum_part1)
    print(sum_part2)

if __name__ == "__main__":
    main()
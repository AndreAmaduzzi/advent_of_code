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


def main():

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        elf1, elf2 = line.split(',')
        if elf2[-1] == '\n':
            elf2 = elf2[:-1]
        elf1 = calc_range(elf1)
        elf2 = calc_range(elf2)

        if check_range(elf1, elf2):
            sum += 1


    print(sum)

if __name__ == "__main__":
    main()
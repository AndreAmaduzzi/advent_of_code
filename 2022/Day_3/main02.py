'''
3st December, 2022
'''

import string

def item_duplicate(group: str) -> list:
    
    lst = []
    for i in group[0]:
        if i in group[1] and i in group[2] and i not in lst:
            lst.append(i)

    return lst


def duplicate_value(d: str) -> int:

    count = 0
    lowercase_element = list(string.ascii_lowercase)
    uppercase_element = list(string.ascii_uppercase)

    for item in d:
        if item in lowercase_element:
            for value, ascii_item in enumerate(lowercase_element):
                if item == ascii_item:
                    count += value + 1
        elif item in uppercase_element:
            for value, ascii_item in enumerate(uppercase_element):
                if item == ascii_item:
                    count += value + 27
    return count


def main():

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    sum = 0
    count_r = 0
    group = []
    for line in lines:

        group.append(line[:-1])
        count_r += 1

        if count_r == 3:
            duplicates = item_duplicate(group)
            # print(duplicates)
            sum += duplicate_value(duplicates)
            group = []
            count_r = 0

    print(sum)

if __name__ == "__main__":
    main()
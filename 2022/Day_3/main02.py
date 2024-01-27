'''
3st December, 2022
'''

import string

def item_duplicate(ruck: str) -> list:
    lst = []
    delimiter = round((len(ruck) - 1) // 2)
    s_1 = [ruck[i] for i in range(0, delimiter)]
    if (len(ruck) - 1) % 2 != 0:
        delimiter += 1
    s_2 = [ruck[i] for i in range(delimiter, len(ruck) - 1)]

    for i in s_1:
        if i in s_2 and i not in lst:
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
    for line in lines:
        duplicates = item_duplicate(line)
        sum += duplicate_value(duplicates)
        print(duplicates)

    print(sum)

if __name__ == "__main__":
    main()
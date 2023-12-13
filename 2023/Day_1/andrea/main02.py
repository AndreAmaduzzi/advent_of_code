"""
1st December, 2023
"""
import re


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    sum = 0
    string = ""
    num_in_letter = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for idx_line, line in enumerate(lines):
        dec = 0
        un = 0
        min = 100000
        max = -1
        min_id = 0
        max_id = 0
        for word in num_in_letter:
            if line.find(word) >= 0:
                occurence = [_.start() for _ in re.finditer(word, line)]
                for x in occurence:
                    if x < min and x >= 0:
                        min_id = num_in_letter[word]
                        min = x
                    if x > max and x >= 0:
                        max_id = num_in_letter[word]
                        max = x

        if min_id >= 0:
            dec = min_id
        if max_id >= 0:
            un = max_id

        if un == 0 and dec != 0:
            un = dec
            max_id = min_id
            max = min

        for idx, ch in enumerate(line):
            if ch.isdecimal():
                if idx < min:
                    min = idx
                    dec = int(ch)
                if idx > max:
                    max = idx
                    un = int(ch)

        if un == 0:
            un = dec
        num = 10 * dec + un
        sum += num

    print("Soluzione:")
    print(sum)


if __name__ == "__main__":
    main()

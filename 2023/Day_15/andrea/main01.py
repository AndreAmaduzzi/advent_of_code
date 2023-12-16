"""
15th December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        words = f.read().split(',')

    sum = 0
    for word in words:
        count = 0
        for ch in word:
            count = ((ord(ch) + count) * 17) % 256
        sum += count

    print('Soluzione:')
    print(sum)


if __name__ == "__main__":
    main()
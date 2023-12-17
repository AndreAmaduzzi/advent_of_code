"""
12th December, 2023
"""

from functools import cache

@cache
def recurse(lava, springs, result=0):
    if not springs:
        return '#' not in lava
    current, springs = springs[0], springs[1:]
    for i in range(len(lava) - sum(springs) - len(springs) - current + 1):
        if "#" in lava[:i]:
            break
        if (nxt := i + current) <= len(lava) and '.' not in lava[i : nxt] and lava[nxt : nxt + 1] != "#":
            result += recurse(lava[nxt + 1:], springs)
    return result

def main():

    with open("input.txt", "r") as file:
        data = [x.split() for x in file.read().splitlines()]
        sum = 0
        for e, (lava, springs) in enumerate(data):
            springs = tuple(map(int, springs.split(",")))
            sum += recurse("?".join([lava] * 5), springs * 5)

    print("Soluzione:")
    print(sum)


if __name__ == "__main__":
    main()

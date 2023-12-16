"""
15th December, 2023
"""

def hash(word):
    count = 0
    for ch in word:
        count = ((ord(ch) + count) * 17) % 256
    return count


def main():
    with open("input.txt", "r") as f:
        words = f.read().strip().split(',')

    sum = 0

    lenses = [[] for i in range(256)]
    lenslengths = [{} for i in range(256)]

    for i, word in enumerate(words):
        label = word.split("=")[0].split("-")[0]
        v = hash(label)
        if "-" in word:
            if label in lenses[v]:
                lenses[v].remove(label)
        if "=" in word:
            if label not in lenses[v]:
                lenses[v].append(label)
            lenslengths[v][label] = int(word.split("=")[1])
    
    for box, lns in enumerate(lenses):
        for i, lens in enumerate(lns):
            sum += (box + 1) * (i + 1) * lenslengths[box][lens]
    
    print('Soluzione:')
    print(sum)


if __name__ == "__main__":
    main()
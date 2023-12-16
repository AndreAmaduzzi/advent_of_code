import numpy as np
from utils import load_data

map_ = {"#": -1, "O": 0, ".": 1}
array = np.array([[map_[char] for char in line] for line in load_data()])
nrows, ncols = array.shape


def roll(array):
    for i in range(ncols):
        rocks = [-1] + list(np.where(array[:, i] == -1)[0]) + [None]
        for j in range(len(rocks) - 1):
            left, right = rocks[j] + 1, rocks[j + 1]
            array[left:right, i] = np.sort(array[left:right, i])
    return array

def cycle(array):
    for i in range(4):
        array = roll(array)
        array = np.rot90(array, -1)
    return array

def hash_(array):
    return tuple(array.ravel())

def score(array):
    rolls = np.where(array == 0)[0]
    return (nrows - rolls).sum()

if __name__ == "__main__":
    seen, scores = {}, {}
    maxval = 1_000_000_000
    for i in range(maxval):
        h = hash_(array)
        if h in seen:
            break
        seen[h] = i
        scores[i] = score(array)
        array = cycle(array)
    cycle_length = i - seen[h]
    index = seen[h] + (maxval - seen[h]) % cycle_length
    print(array)
    print(scores[index])
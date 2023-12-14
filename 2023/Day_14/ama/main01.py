import numpy as np
from utils import load_data

map_ = {"#": -1, "O": 0, ".": 1}
array = np.array([[map_[char] for char in line] for line in load_data()])
nrows, ncols = array.shape

def score(array):
    rolls = np.where(array == 0)[0]
    return (nrows - rolls).sum()

def roll(array):
    for i in range(ncols):
        rocks = [-1] + list(np.where(array[:, i] == -1)[0]) + [None]
        for j in range(len(rocks) - 1):
            left, right = rocks[j] + 1, rocks[j + 1]
            array[left:right, i] = np.sort(array[left:right, i])
    return array

if __name__ == "__main__":
    print(score(roll(array)))
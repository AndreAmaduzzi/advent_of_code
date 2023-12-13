"""
11th December, 2023
"""
import numpy as np


def main():
    with open("test.txt", "r") as f:
        grid = f.read()

    galaxy_map = np.array([list(line) for line in grid.split("\n")])
    expand_rows = np.array([])
    expand_cols = np.array([])

    for i in range(galaxy_map.shape[0]):
        if not "#" in galaxy_map[i, :]:
            expand_rows = np.append(expand_rows, i)

    for j in range(galaxy_map.shape[1]):
        if not "#" in galaxy_map[:, j]:
            expand_cols = np.append(expand_cols, j)

    galaxies = list(zip(*np.where(galaxy_map == "#")))

    total_distance = 0
    distance_mult = 1000000 - 1
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total_distance += abs(
                galaxies[i][0] - galaxies[j][0]
            ) + distance_mult * len(
                expand_rows[
                    (min(galaxies[i][0], galaxies[j][0]) < expand_rows)
                    & (max(galaxies[i][0], galaxies[j][0]) > expand_rows)
                ]
            )
            total_distance += abs(
                galaxies[i][1] - galaxies[j][1]
            ) + distance_mult * len(
                expand_cols[
                    (min(galaxies[i][1], galaxies[j][1]) < expand_cols)
                    & (max(galaxies[i][1], galaxies[j][1]) > expand_cols)
                ]
            )

    print("Soluzione:")
    print(total_distance)


if __name__ == "__main__":
    main()

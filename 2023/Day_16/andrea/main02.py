"""
16th December, 2023
"""

from collections import defaultdict

def main():

    RIGHT, LEFT, UP, DOWN = (1, 0), (-1, 0), (0, -1), (0, 1)

    MOVES = {
        (".", RIGHT): [RIGHT],
        (".", LEFT): [LEFT],
        (".", UP): [UP],
        (".", DOWN): [DOWN],

        ("-", RIGHT): [RIGHT],
        ("-", LEFT): [LEFT],
        ("-", UP): [LEFT, RIGHT],
        ("-", DOWN): [LEFT, RIGHT],

        ("|", RIGHT): [UP, DOWN],
        ("|", LEFT): [UP, DOWN],
        ("|", UP): [UP],
        ("|", DOWN): [DOWN],

        ("\\", RIGHT): [DOWN],
        ("\\", LEFT): [UP],
        ("\\", UP): [LEFT],
        ("\\", DOWN): [RIGHT],

        ("/", RIGHT): [UP],
        ("/", LEFT): [DOWN],
        ("/", UP): [RIGHT],
        ("/", DOWN): [LEFT],
    }

    with open('input.txt') as f:
        tiles = [list(line.strip()) for line in f.readlines()]

        energized_max = -1

        beam_starts = [((-1, y), RIGHT) for y in range(len(tiles))]
        beam_starts += [((len(tiles[0]), y), LEFT) for y in range(len(tiles))]
        beam_starts += [((x, -1), DOWN) for x in range(len(tiles[0]))]
        beam_starts += [((x, len(tiles)), DOWN) for x in range(len(tiles[0]))]

        for beam_start in beam_starts:

            energized = defaultdict(set)
            beams = [beam_start]

            while len(beams) > 0:
                beam_pos, dir = beams.pop()
                x, y = (beam_pos[0] + dir[0], beam_pos[1] + dir[1])

                if x < 0 or x >= len(tiles[0]) or y < 0 or y >= len(tiles):
                    # beam escapes
                    continue

                if (x, y) in energized and dir in energized[(x, y)]:
                    # beam in this direction already passed
                    continue

                energized[(x, y)].add(dir)

                for new_dir in MOVES[(tiles[y][x], dir)]:
                    beams.append(((x, y), new_dir))

            energized_max = max(energized_max, len(energized))

        print('Soluzione:')
        print(energized_max)


if __name__ == "__main__":
    main()
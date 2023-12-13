"""
2nd December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    sum = 0
    id_game = 0
    ref_red = 12
    ref_green = 13
    ref_blue = 14
    for line in lines:
        state_word = 0
        aux_n = 0
        correct = True
        for word in line.split():
            if state_word == 0:
                state_word = 1
            elif state_word == 1:
                id_game = int(word[:-1])
                state_word = 2
            elif state_word == 2:
                aux_n = int(word)
                state_word = 3
            elif state_word == 3:
                if word[:-1] == "red" or word == "red":
                    if aux_n > ref_red:
                        correct = False
                elif word[:-1] == "blue" or word == "blue":
                    if aux_n > ref_blue:
                        correct = False
                elif word[:-1] == "green" or word == "green":
                    if aux_n > ref_green:
                        correct = False
                state_word = 2

        if correct:
            sum += id_game

    print(sum)


if __name__ == "__main__":
    main()

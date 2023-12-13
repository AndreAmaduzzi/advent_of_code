"""
2nd December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    sum = 0
    id_game = 0
    for line in lines:
        state_word = 0
        aux_n = 0
        n_red = 0
        n_blue = 0
        n_green = 0
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
                    if aux_n > n_red:
                        n_red = aux_n
                elif word[:-1] == "blue" or word == "blue":
                    if aux_n > n_blue:
                        n_blue = aux_n
                elif word[:-1] == "green" or word == "green":
                    if aux_n > n_green:
                        n_green = aux_n
                state_word = 2

        # print(
        #     "Set of "
        #     + str(n_red)
        #     + " red, "
        #     + str(n_blue)
        #     + " blue, "
        #     + str(n_green)
        #     + " green"
        # )
        pow = n_red * n_blue * n_green
        # print(pow)
        sum += pow

    print(sum)


if __name__ == "__main__":
    main()

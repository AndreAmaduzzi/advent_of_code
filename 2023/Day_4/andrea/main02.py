"""
4th December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    n_game = len(lines)
    id_game = 0
    copy_cards = [0] * n_game

    for line in lines:
        win_set = set()
        state_word = 0
        first = True
        count_win = 0
        for word in line.split():
            if state_word == 0:
                if (word == 'Card'):
                    state_word = 1
                else:
                    print('Error(1)')
                    break
            elif state_word == 1:
                id_game = int(word[:-1])
                state_word = 2
            elif state_word == 2:
                if (word.isdecimal()):
                    win_set.add(int(word))
                elif (word == '|'):
                    state_word = 3
                else:
                    print('Error(3)')
            elif state_word == 3:
                if int(word) in win_set:
                    count_win += 1

        copy_cards[id_game-1] += 1
        if count_win > 0: 
            for it in range(count_win):
                if copy_cards[id_game-1] == 0:
                    copy_cards[id_game-1] = 1
                copy_cards[id_game+it] += (1 * copy_cards[id_game-1])

        win_set = ()

    sum = 0
    for i in copy_cards:
        sum += i
    print('Soluzione:')
    print(sum)


if __name__ == "__main__":
    main()
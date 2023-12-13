"""
4th December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    sum = 0
    id_game = 0

    for line in lines:
        win_set = set()
        state_word = 0
        first = True
        points = 0
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
                if first:
                    if int(word) in win_set:
                        first = False
                        points += 1
                else:
                    if int(word) in win_set:
                        points *= 2

        sum += points        
        win_set = ()

    print('Soluzione:')
    print(sum)


if __name__ == "__main__":
    main()
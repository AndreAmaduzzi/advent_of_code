'''
2st December, 2022
'''

WINS = {'X': 'C',
        'Y': 'A',
        'Z': 'B'}

LOSS = {'X': 'B',
        'Y': 'C',
        'Z': 'A'}


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        
    points = 0
    for idx, line in enumerate(lines):
        enemy = line[0]
        me = line[2]
        if WINS[me] == enemy:
            points += 6
        elif LOSS[me] == enemy:
            points += 0
        else:
            points += 3

        if me == 'X':
            points += 1
        elif me == 'Y':
            points += 2
        else:
            points += 3

            
    print('Soluzione:')
    print(points)
            
    
if __name__ == "__main__":
    main()
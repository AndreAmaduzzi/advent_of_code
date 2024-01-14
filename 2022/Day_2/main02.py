'''
2st December, 2022
'''

WINS = {'C': 'X',
        'A': 'Y',
        'B': 'Z'}

LOSS = {'B': 'X',
        'C': 'Y',
        'A': 'Z'}

DRAW = {'A': 'X',
        'B': 'Y',
        'C': 'Z'}

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        
    points = 0
    for idx, line in enumerate(lines):
        enemy = line[0]
        me = line[2]
        if line[2] == 'X':
            me = LOSS[enemy]
        elif line[2] == 'Y':
            me = DRAW[enemy]
            points += 3
        else:
            me = WINS[enemy]
            points += 6

        print(me)

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
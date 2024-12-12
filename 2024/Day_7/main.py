"""
7st December, 2024
"""

import itertools

def get_all_combinations(numbers, target):
    operations = ['+', '*', '||']

    # Genera tutte le possibili combinazioni di operazioni
    for ops in itertools.product(operations, repeat=len(numbers)-1):
        expression = numbers[0]
        for i in range(len(ops)):
            if ops[i] == '+':
                expression += numbers[i+1]
            elif ops[i] == '*':
                expression *= numbers[i+1]
            elif ops[i] == '||':
                expression = int(str(expression) + str(numbers[i+1]))
        if expression == int(target):
            return expression
        
    return 0

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    values = [line.split() for line in lines]
    targets = [int(v[0][:-1]) for v in values]
    nums = [[int(v[i]) for i in range(1, len(v))] for v in values]
   
    somma = 0
    for num, target in zip(nums, targets):
        somma = somma + get_all_combinations(num, target)

    print(somma)


if __name__ == "__main__":
    main()

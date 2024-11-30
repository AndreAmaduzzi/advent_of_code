'''
10st December, 2022
'''

def process_sprite(cycle, row, x):
    mid = cycle % 40
    # Are we about to enter a new row?
    if not mid:
        row += 1
        print()
        return
    if mid-1 <= x <= mid+1:
        print("#", end='')
    else:
        print(".", end='')

def main():
    with open("input.txt") as f:
        rows = f.readlines()

    x = 1
    cycle = 0
    row = 0
    values = [1]

    for line in rows:
        cmd = line.split()[0]
        if (cmd == "addx"):
            value = (int) (line.split()[1])
        
        if (cmd == "noop"):
            values.append(values[-1])
            
        elif (cmd == "addx"):
            value = int(value)
            values.append(values[-1])
            values.append(values[-1] + value)

    print(len(values))

    cycle = 0
    while cycle < len(values):
        xval = values[cycle]
        if abs(xval - (cycle%40)) < 2:
            print('#',end='')
        else:
            print('.',end='')
        cycle += 1
        if cycle % 40 == 0:
            print("")


if __name__ == "__main__":
    main()
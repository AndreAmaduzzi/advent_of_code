'''
10st December, 2022
'''

def main():
    with open("input.txt") as f:
        rows = f.readlines()

    cycle = 0
    X = 1
    cycle_sampling = 20
    signal_strength = 0
    for line in rows:
        cmd = line.split()[0]
        if (cmd == "addx"):
            value = (int) (line.split()[1])
        
        if (cmd == "noop"):
            cycle += 1
            if (cycle >= cycle_sampling):
                signal_strength += cycle_sampling * X
                cycle_sampling += 40
        elif (cmd == "addx"):
            value = int(value)
            if (cycle + 1 >= cycle_sampling):
                signal_strength += cycle_sampling * X
                cycle_sampling += 40
            cycle += 2
            if (cycle >= cycle_sampling):
                signal_strength += cycle_sampling * X
                cycle_sampling += 40
            X += value

        if (cycle >= 220):
            break

    print(signal_strength)
    

if __name__ == "__main__":
    main()
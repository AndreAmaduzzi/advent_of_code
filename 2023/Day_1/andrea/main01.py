'''
1st December, 2023
'''

def main():

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    sum=0
    for line in lines:
        first = True
        for ch in line:
            if ch.isdecimal() and first:
                dec = int(ch)
                un = dec
                first = False
            elif ch.isdecimal():
                un = int(ch)

        num = 10 * dec + un
        sum += num

    print(sum)

if __name__ == "__main__":
    main()
'''
1st December, 2022
'''


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    sum=0
    max=0
    for line in lines:
        if line != "\n":
            sum += int(line)
        else:
            if sum>max:
                max=sum
            sum=0
            
    print('max:', max)
            
        

if __name__ == "__main__":
    main()
'''
1st December, 2022
'''

def main():
    maxes = [0, 0, 0]
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        
    current_sum = 0
    for idx, line in enumerate(lines):
        if line != "\n" and idx!=len(lines)-1:
            current_sum += int(line)
        else:
            if idx==len(lines)-1 and line != "\n":
                current_sum += int(line)
            if current_sum>maxes[0]:
                maxes[0]=current_sum
                maxes.sort()
            current_sum=0
            
    print(maxes)
    print(sum(maxes))
            
    
if __name__ == "__main__":
    main()
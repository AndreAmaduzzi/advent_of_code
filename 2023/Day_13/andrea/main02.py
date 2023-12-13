"""
13th December, 2023
"""
# import numpy as np

def find_reflection(current_lines):
    reflection=False
    idx=0
    while not reflection and idx<len(current_lines)-1:
        count_wrong = 0
        n_lines = min(idx+1, len(current_lines)-idx-1)
        count_ok = 0
        for i in range(0, n_lines):
            count_char=0
            for i_char in range(0, len(current_lines[idx-1])):
                if current_lines[idx-i][i_char]==current_lines[idx+i+1][i_char]:
                    count_char += 1
                    if count_char == len(current_lines[idx-1]):
                        count_ok +=1    # strings are identical
                        break
                else:
                    count_wrong += 1
                    if count_wrong>1:
                        break
            if count_wrong>1:
                break
        if count_wrong==1:
            reflection=True
        idx += 1
    return reflection, idx

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    lines.append("\n")

    current_rows = []
    sum = 0
    for line in lines:
        if line == "\n":            
            # logic for rows
            row_reflection, row_reflect_idx = find_reflection(current_rows)

            if not row_reflection:
                current_columns = []
                # get columns
                for row_i in range(0, len(current_rows[0])-1):    # loop over chars
                    column = ''
                    for row_j in range(0, len(current_rows)):   # loop over rows
                        column += current_rows[row_j][row_i]
                    current_columns.append(column)

                # logic of columns
                col_reflection, col_reflect_idx = find_reflection(current_columns)
                
                if col_reflection:
                    sum += col_reflect_idx
                    
                # riflesso verticale => sommi colonne a sx
                # riflesso orizzontale => sommi colonne sopra e moltiplichi per 100
            else:
                sum += (row_reflect_idx)*100
                
            current_rows.clear()  
        else:
            current_rows.append(line)
        
    print('sum: ', sum)
    print('exp 405')

if __name__ == "__main__":
    main()
'''
8st December, 2022
'''

def check_visible_tree(trees, height):
    for i in range(len(trees)):
        if (height <= trees[i]):
            return False
    return True

def get_visible_tree_distance(trees, height):
    for i in range(len(trees)):
        if (height > trees[i]):
            continue
        else:
            break
    return i + 1

def main():
    with open("input.txt") as f:
        rows = f.readlines()

    # Remove the last character (newline) from each row
    rows = [row.strip() for row in rows]

    edge_size = len(rows) * 2 + (len(rows[0]) - 2) * 2

    columns = []
    # get columns
    for row_i in range(0, len(rows[0])-1):    # loop over chars
        column = ''
        for row_j in range(0, len(rows)):   # loop over rows
            column += rows[row_j][row_i]
        columns.append(column)

    print(rows[:0])

    # Get visible trees
    n_visibles = 0
    for i in range(1, len(rows[0]) - 1):
        for j in range(1, len(columns[0]) - 1):
            if check_visible_tree(rows[i][:j], rows[i][j]) or check_visible_tree(rows[i][j+1:], rows[i][j]) or check_visible_tree(columns[j][:i], rows[i][j]) or check_visible_tree(columns[j][i+1:], rows[i][j]):
                n_visibles += 1            

    n_visibles += edge_size
    print(n_visibles)

    # Get visible trees distance score
    score_distance = 0
    for i in range(1, len(rows[0]) - 1):
        for j in range(1, len(columns[0]) - 1):
            look_left_dist = get_visible_tree_distance(rows[i][:j][::-1], rows[i][j])
            look_right_dist = get_visible_tree_distance(rows[i][j+1:], rows[i][j])
            look_up_dist =  get_visible_tree_distance(columns[j][:i][::-1], rows[i][j])
            look_down_dist = get_visible_tree_distance(columns[j][i+1:], rows[i][j])
            act_distance = look_left_dist * look_right_dist * look_up_dist * look_down_dist
            if (act_distance > score_distance):
                score_distance = act_distance

    print(score_distance)

if __name__ == "__main__":
    main()
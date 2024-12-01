"""
1st December, 2024
"""


def main():
    with open("input.txt") as f:
        rows = f.readlines()

    # Remove the last character (newline) from each row
    rows = [row.strip() for row in rows]

    columns = []
    # get columns
    for row_i in range(0, len(rows[0].split())):  # loop over chars
        column = []
        for row_j in range(0, len(rows)):  # loop over rows
            temp = rows[row_j].split()[row_i]
            column.append((int)(temp))
        columns.append(column)

    columns[0].sort()
    columns[1].sort()

    sum = 0
    for i in range(len(columns[0])):
        sum += abs(columns[0][i] - columns[1][i])

    print(sum)

    sum_2 = 0
    for i in range(len(columns[0])):
        count = columns[1].count(columns[0][i])
        sum_2 += columns[0][i] * count

    print(sum_2)


if __name__ == "__main__":
    main()

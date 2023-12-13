"""
9th December, 2023
"""


def main():
    with open("input.txt", "r") as f:
        lines = f.read().strip().split("\n")

    temperatures = []
    for line in lines:
        aux_lines = map(int, line.split())
        temperatures.append(list(aux_lines))

    # print(temperatures)

    sum = 0
    for scan in temperatures:
        diff = scan
        extra_val = 0
        while any(diff):
            extra_val += diff[-1]
            diff_aux = []
            for id in range(len(diff)):
                if id < len(diff) - 1:
                    diff_aux.append(diff[id + 1] - diff[id])
            diff = diff_aux
            # print(diff)
        sum += extra_val

    print("Soluzione:")
    print(sum)


if __name__ == "__main__":
    main()

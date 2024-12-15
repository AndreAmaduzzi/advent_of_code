"""
9st December, 2024
"""


def sort_list(memory):
    for i in range(len(memory) - 1, -1, -1):
        if memory[i] != ".":
            for j in range(i):
                if memory[j] == ".":
                    memory[j], memory[i] = memory[i], "."
                    break
    return memory


def sort_list_blocks(memory):
    n = len(memory)
    i = n - 1
    while i > 0:
        if memory[i] != ".":
            end = i + 1
            while i > 0 and memory[i] == memory[end - 1]:
                i -= 1
            start = i + 1
            block_size = end - start
            j = 0
            s = 0
            while j >= 0 and j < start and s < block_size:
                if memory[j] == ".":
                    s += 1
                else:
                    s = 0
                j += 1
            if s == block_size:
                memory[j - s : j] = memory[start:end]
                memory[start:end] = "." * s
        else:
            i -= 1
    return memory


def check_sum(memory):
    sum = 0
    for i in range(len(memory)):
        if memory[i] != ".":
            sum += i * int(memory[i])
    return sum


def main():
    with open("input.txt") as f:
        lines = f.read()

    ID = 0
    is_space = False
    memory = []
    for ch in lines:
        if is_space:
            spaces = ["." for i in range(int(ch))]
            memory.extend(spaces)
            is_space = False
        else:
            values = [str(ID) for i in range(int(ch))]
            memory.extend(values)
            ID += 1
            is_space = True

    print(memory)
    memory2 = memory.copy()

    sort_list(memory)
    res = check_sum(memory)
    print(res)

    sort_list_blocks(memory2)
    res2 = check_sum(memory2)
    print(res2)


if __name__ == "__main__":
    main()

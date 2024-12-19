"""
11st December, 2024
"""



memory = {}

def solve(stone, blinks):
    if blinks == 0:
        return 1
    elif (stone, blinks) in memory:
        return memory[(stone, blinks)]
    elif stone == 0:
        val = solve(1, blinks - 1)
    elif len(str_stone := str(stone)) % 2 == 0:
        mid = len(str_stone) // 2
        val = solve(int(str_stone[:mid]), blinks - 1) + solve(int(str_stone[mid:]), blinks - 1)
    else:
        val = solve(stone * 2024, blinks - 1)
    memory[(stone, blinks)] = val
    return val


def main():
   with open("input.txt") as f:
      lines = f.read()

   stones = [int(stone) for stone in lines.split()]

   sum = 0
   for i in range(len(stones)):
      sum += solve(stones[i], 75)

   print(sum)

if __name__ == "__main__":
    main()

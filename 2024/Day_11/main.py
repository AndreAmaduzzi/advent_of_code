"""
11st December, 2024
"""

blinks = 25


def divide_stone(num):
   num = str(num)
   half_length = len(num) // 2
   first_half = int(num[:half_length])
   second_half = int(num[half_length:])
   return first_half, second_half

def get_blink_action(stones):
   i = 0
   while i < len(stones):
      if stones[i] == 0:
         stones[i] = 1
      elif len(str(stones[i])) % 2 == 0:
         stone1, stone2 = divide_stone(stones[i])
         stones[i:i] = [stone1, stone2]
         stones.pop(i+2)
         i += 1
      else:
         stones[i] *= 2024
      i += 1
   return stones

def main():
   with open("input.txt") as f:
      lines = f.read()

   stones = [int(stone) for stone in lines.split()]

   for i in range(blinks):
      stones = get_blink_action(stones)

   print(len(stones))

if __name__ == "__main__":
    main()

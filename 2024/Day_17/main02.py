"""
17st December, 2024
"""

import re

def main():
   with open("test.txt") as f:
      lines = f.read()

   numbers = [int(n) for n in re.findall(r"\d+", lines)][-1:2:-1]

   def next_number(a, i):
      if i == len(numbers):
         print(a)
         quit()
      a2 = a << 3
      for b in range(8):
         if (b ^ (a2 + b >> (b ^ 7))) % 8 == numbers[i]: next_number(a2 + b, i + 1)

   next_number(0, 0)

if __name__ == "__main__":
    main()
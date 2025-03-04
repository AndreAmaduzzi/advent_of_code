"""
19st December, 2024
"""

from functools import cache

def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.read()

   towels, designs =  lines.split('\n\n')
   towels = set(towels.split(', '))

   @cache
   def count_ways(design: str):
       if not design:
           return 1

       combinations = 0
       for towel in towels:
           if design.startswith(towel):
               combinations += count_ways(design[len(towel):])

       return combinations

   print(sum(map(count_ways, designs.split('\n'))))


if __name__ == "__main__":
    main()

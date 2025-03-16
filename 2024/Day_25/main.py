"""
25st December, 2024
"""

from collections import defaultdict

def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.read()

   locks_and_keys = defaultdict(list)

   for seg in lines.split('\n\n'):
       locks_and_keys[seg[0]].append([
           col.count('#') for col in zip(*seg.split('\n'))
       ])

   fit = 0
   for lock in locks_and_keys['.']:
       for key in locks_and_keys['#']:
           fit += all(i + j < 8 for i, j in zip(lock, key))
   
   print(fit)

if __name__ == "__main__":
    main()

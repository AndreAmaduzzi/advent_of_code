'''
14st December, 2022
'''

scan = set()
depth = 0

def space(x: int, y: int) -> tuple or None:
   global depth
   for dx in 0, -1, 1:  # y doesn't change
      if (x + dx, y) not in scan and y < depth + 2:
         return x + dx, y
   scan.add((x, y - 1))  # sand      None


def loop(sand: int, level: int) -> int:
   while sand := sand + 1:
      x, y = 500, 0
      while xy := space(x, y + 1):
         x, y = xy[0], xy[1]
      if y == level:  return sand


def main():
   global depth
   with open("input.txt") as f:
      cave = [[[int(a) for a in b.split(',')] for b in c.split('->')]  \
         for c in f.read().splitlines()]

   for path in cave:
      for XY in zip(path, path[1:]):
         for x in range(min(XY)[0], max(XY)[0] + 1):
            for y in range(min(XY)[1], max(XY)[1] + 1):
               scan.add((x, y))  # rock
   depth = max([xy[1] for xy in scan])

   print('P1=', (sand := loop(0, depth))-4)
   print('P2=', loop(sand, 0))

if __name__ == "__main__":
    main()






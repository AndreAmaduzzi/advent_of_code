"""
18st December, 2024
"""

from collections import deque

def get_directions(map, x, y, old_dir=None):
   dirs = []
   if x+1 < len(map[0]):
      if map[y][x+1] == "." and old_dir != "<":
         dirs.append(">")
   if x-1 >= 0:
      if map[y][x-1] == "." and old_dir != ">":
         dirs.append("<")
   if y+1 < len(map):
      if map[y+1][x] == "." and old_dir != "^":
         dirs.append("v")
   if y-1 >= 0:
      if map[y-1][x] == "." and old_dir != "v":
         dirs.append("^")
   return dirs

def beautiful_print(_map):
    for _row in _map:
        print(''.join(_row))

def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.readlines()

   if source == "test.txt":
      corrupted = 12
      size = 6
   else:
      corrupted = 1024
      size = 70

   map = [['.' for i in range(size+1)] for j in range(size+1)]
   for i in range(corrupted):
      coord = [int(num) for num in lines[i][:-1].split(',')]
      map[coord[1]][coord[0]] = '#' 

   #beautiful_print(map)

   queue = deque()
   queue.append((0, 0, 0))
   visited = set()
   moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

   while queue:
        x, y, length = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == (size, size):
            break
        for move in moves:
            if 0 <= x + move[0] <= size and 0 <= y + move[1] <= size and map[x + move[0]][y + move[1]] == ".":
                queue.append((x + move[0], y + move[1], length + 1))

   print(length)


if __name__ == "__main__":
    main()

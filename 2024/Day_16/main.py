"""
16st December, 2024
"""

import sys
sys.setrecursionlimit(3000)

direction = {
   "<": (-1,0),
   ">": (1,0),
   "^": (0,-1),
   "v": (0,1)
}

def get_directions(map, x, y, old_dir=None):
   dirs = []
   if (map[y][x+1] == "." or map[y][x+1] == "E") and old_dir != "<":
      dirs.append(">")
   if (map[y][x-1] == "." or map[y][x-1] == "E") and old_dir != ">":
      dirs.append("<")
   if (map[y+1][x] == "." or map[y+1][x] == "E") and old_dir != "^":
      dirs.append("v")
   if (map[y-1][x] == "." or map[y-1][x] == "E") and old_dir != "v":
      dirs.append("^")
   return dirs

def init_path(map):
   for j, row in enumerate(map):
      for i, cell in enumerate(row):
         if cell == "S":
            x = i
            y = j
   dirs = get_directions(map, x, y)
   return x, y, dirs

def path_iter(map, x, y, dir, points, pos_cross):
   while map[y][x] != "E":
      dx, dy = direction[dir]
      x += dx
      y += dy
      points += 1
      if map[y][x] == "E":
         return points
      dirs = get_directions(map, x, y, dir)
      if len(dirs) > 1:
         points_dir = []
         for mov in dirs:
            res = 0
            if (x, y, mov) in pos_cross:
               res = pos_cross[(x, y, mov)]
            else:
               pos_cross[(x, y, mov)] = 1e9
               res = path_iter(map, x, y, mov, res, pos_cross)
            if res != -1 and (res < pos_cross[(x, y, mov)]):
               pos_cross[(x, y, mov)] = res
            if mov != dir:
               res += 1000
            points_dir.append(res)
         points += min(points_dir)
         return points
      elif len(dirs) == 0:
         return 1e9
      else:
         if dirs[0] != dir:
            points += 1000
            dir = dirs[0]
   
   return points

def main():
   with open("input.txt") as f:
      lines = f.readlines()

   map = [list(row[:-1]) for row in lines]

   x, y, dirs = init_path(map)

   print(x, y, dirs)

   pos_cross = {}
   points = 1e9
   for dir in dirs:
      res = 0
      if dir != "<":
         res += 1000
      res = path_iter(map, x, y, dir, res, pos_cross)
      if res != -1 and res < points:
         points = res

   print(points)


if __name__ == "__main__":
    main()

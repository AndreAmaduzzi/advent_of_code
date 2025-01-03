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

def path_iter(map, x, y, dir, points, pos_cross, last_cross):
   x_m1, y_m1 = last_cross
   while map[y][x] != "E":
      dx, dy = direction[dir]
      x += dx
      y += dy
      points += 1
      if (x, y) in pos_cross:
         if (x_m1, y_m1) in pos_cross[(x, y)]:
            if pos_cross[(x, y)][(x_m1, y_m1)] == -1:
               return -1
            else:
               return points + pos_cross[(x, y)][(x_m1, y_m1)]
      elif map[y][x] == "E":
         return points
      dirs = get_directions(map, x, y, dir)
      if len(dirs) > 1:
         if (x, y) not in pos_cross:
            pos_cross[(x, y)] = {}
         pos_cross[(x, y)][(x_m1, y_m1)] = -1
         for mov in dirs:
            res = 0
            if mov != dir:
               res += 1000
            res = path_iter(map, x, y, mov, res, pos_cross, (x, y))
            if res != -1 and (res < pos_cross[(x, y)][(x_m1, y_m1)] or pos_cross[(x, y)][(x_m1, y_m1)] == -1):
               pos_cross[(x, y)][(x_m1, y_m1)] = res
         if pos_cross[(x, y)][(x_m1, y_m1)] == -1:
            return -1
         else:
            points += pos_cross[(x, y)][(x_m1, y_m1)]
            return points
      elif len(dirs) == 0:
         return -1
      else:
         if dirs[0] != dir:
            points += 1000
            dir = dirs[0]
   
   return points

def main():
   with open("test1.txt") as f:
      lines = f.readlines()

   map = [list(row[:-1]) for row in lines]

   x, y, dirs = init_path(map)

   print(x, y, dirs)

   last_cross = (x, y)
   pos_cross = {}
   points = -1
   for dir in dirs:
      res = 0
      if dir != "<":
         res += 1000
      res = path_iter(map, x, y, dir, res, pos_cross, last_cross)
      if res != -1 and (res < points or points == -1):
         points = res

   print(points)


if __name__ == "__main__":
    main()

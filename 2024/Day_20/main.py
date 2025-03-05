"""
20st December, 2024
"""


def init_path(map):
   for j, row in enumerate(map):
      for i, cell in enumerate(row):
         if cell == "S":
            x = i
            y = j
            break
   return x, y


direction = {
   "<": (-1,0),
   ">": (1,0),
   "^": (0,-1),
   "v": (0,1)
}


def get_direction(map, x, y, old_dir=None):
   if (map[y][x+1] == "." or map[y][x+1] == "E") and old_dir != "<":
      return ">"
   if (map[y][x-1] == "." or map[y][x-1] == "E") and old_dir != ">":
      return "<"
   if (map[y+1][x] == "." or map[y+1][x] == "E") and old_dir != "^":
      return "v"
   if (map[y-1][x] == "." or map[y-1][x] == "E") and old_dir != "v":
      return "^"
   return None


def path_iter(map, x, y):
   score = {}
   score[(x, y)] = 0
   path = []
   count = 0
   old_dir = None
   while map[y][x] != "E":
      dir = get_direction(map, x, y, old_dir)
      path.append(dir)
      dx, dy = direction[dir]
      x += dx
      y += dy
      count += 1
      score[(x, y)] = count
      old_dir = dir
   return score, path


def calc_cheats(map, score, path, x, y, target):
   cheats = 0
   for i, dir in enumerate(path):

      if map[y-1][x] == "#":
         if (x, y-2) in score:
            if score[(x, y-2)] - score[(x, y)] - 2 >= target:
               cheats += 1
      if map[y+1][x] == "#":
         if (x, y+2) in score:
            if score[(x, y+2)] - score[(x, y)] - 2 >= target:
               cheats += 1
      if map[y][x-1] == "#":
         if (x-2, y) in score:
            if score[(x-2, y)] - score[(x, y)] - 2 >= target:
               cheats += 1
      if map[y][x+1] == "#":
         if (x+2, y) in score:
            if score[(x+2, y)] - score[(x, y)] - 2 >= target:
               cheats += 1
      dx, dy = direction[dir]
      x += dx
      y += dy
   return cheats


def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.readlines()

   map = [list(row[:-1]) for row in lines]

   x, y = init_path(map)
   x_start = x
   y_start = y

   score, path = path_iter(map, x, y)

   res = calc_cheats(map, score, path, x_start, y_start, 100)

   print(res)

if __name__ == "__main__":
    main()

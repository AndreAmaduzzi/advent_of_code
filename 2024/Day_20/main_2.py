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
   count = 0
   old_dir = None
   while map[y][x] != "E":
      dir = get_direction(map, x, y, old_dir)
      dx, dy = direction[dir]
      x += dx
      y += dy
      count += 1
      score[(x, y)] = count
      old_dir = dir
   return score


def calc_cheats(path, threshold):
   cheats = 0
   for t2 in range(threshold, len(path)):
       for t1 in range(t2 - threshold):
           x1, y1 = path[t1]
           x2, y2 = path[t2]
           distance = abs(x1-x2) + abs(y1-y2)
           if distance <= 20 and t2 - t1 - distance >= threshold:
               cheats += 1

   return cheats


def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.readlines()

   map = [list(row[:-1]) for row in lines]

   x, y = init_path(map)

   score = path_iter(map, x, y)
   path = sorted(score, key=score.get)
   res = calc_cheats(path, 100)

   print(res)

if __name__ == "__main__":
    main()

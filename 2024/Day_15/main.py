"""
15st December, 2024
"""

direction = {
   "<": (-1,0),
   ">": (1,0),
   "^": (0,-1),
   "v": (0,1)
}

def robot_pos(grid):
   for y, row in enumerate(grid):
      for x, col in enumerate(row):
         if grid[x][y] == "@":
            return (x, y)
         
def next_move(grid, x, y, dx, dy):
   if grid[y+dy][x+dx] == "O":
      res = next_move(grid, x+dx, y+dy, dx, dy)
      if res:
         grid[y][x], grid[y+dy][x+dx] = grid[y+dy][x+dx], grid[y][x]
         return True
      else:
         return False
   elif grid[y+dy][x+dx] == "#":
      return False
   elif grid[y+dy][x+dx] == ".":
      grid[y][x], grid[y+dy][x+dx] = grid[y+dy][x+dx], grid[y][x]
      return True
   else:
      return False

def count_boxes(grid):
   sum = 0
   for y, row in enumerate(grid):
      for x, col in enumerate(row):
         if grid[y][x] == "O":
            sum += x + y * 100
   
   return sum


def main():
   with open("input.txt") as f:
      lines = f.read()

   tmp_grid, tmp_movs = lines.split("\n\n")
   grid = [list(row) for row in tmp_grid.split("\n")]
   movs = tmp_movs.split("\n")
   x, y = robot_pos(grid)

   #print([x, y])

   for line in movs:
      for mov in line:
         dx, dy = direction[mov]
         res = next_move(grid, x, y, dx, dy)
         if res:
            x += dx
            y += dy
   
   sum_boxes = count_boxes(grid)

   print(sum_boxes)
   


if __name__ == "__main__":
    main()

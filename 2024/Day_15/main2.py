"""
15st December, 2024
"""

direction = {
   "<": (-1,0),
   ">": (1,0),
   "^": (0,-1),
   "v": (0,1)
}

def transform_grid(grid):
   new_grid = []
   for y, row in enumerate(grid):
      new_row = []
      for x, col in enumerate(row):
         if grid[y][x] == "#":
            new_row.extend(["#","#"])
         elif grid[y][x] == "O":
            new_row.extend(["[","]"])
         elif grid[y][x] == ".":
            new_row.extend([".","."])
         elif grid[y][x] == "@":
            new_row.extend(["@","."])
      new_grid.append(new_row)
   return new_grid

def robot_pos(grid):
   for y, row in enumerate(grid):
      for x, col in enumerate(row):
         if grid[y][x] == "@":
            return (x, y)
         
def next_move(grid, x, y, dx, dy, second):
   if grid[y+dy][x+dx] == "[" or grid[y+dy][x+dx] == "]" and grid[y][x] != "." and second == False:
      if dy != 0:
         res1 = next_move(grid, x+dx, y+dy, dx, dy, False)
         if grid[y][x] != "@":
            if grid[y][x] == "[" and grid[y+dy][x+dx] != ".":
               res2 = next_move(grid, x+dx+1, y+dy, dx, dy, True)
            elif grid[y][x] == "]" and grid[y+dy][x+dx] != ".":
               res2 = next_move(grid, x+dx-1, y+dy, dx, dy, True)
            elif grid[y][x] == "[" and (grid[y+dy][x+dx+1] != "." and grid[y+dy][x+dx+1] != "#"):
               res2 = next_move(grid, x+1, y+dy, dx, dy, False)
            elif grid[y][x] == "]" and (grid[y+dy][x+dx-1] != "." and grid[y+dy][x+dx-1] != "#"):
               res2 = next_move(grid, x-1, y+dy, dx, dy, False)
            else:
               res2 = True
         else:
            res2 = True
      else:
         res1 = next_move(grid, x+dx, y+dy, dx, dy, False)
         res2 = True
      if res1 and res2:
         if grid[y][x] == "[" or grid[y][x] == "]" or grid[y][x] == ".":
            if dy == 0 and ((grid[y][x] == "[") or (grid[y][x] == "]" and grid[y+dy][x+dx] != ".")):
               if (dx > 0 and grid[y][x] == "[") or (dx < 0 and grid[y][x] == "]"):
                  grid[y][x], grid[y+dy][x+dx], grid[y+2*dy][x+2*dx] = grid[y+2*dy][x+2*dx], grid[y][x], grid[y+dy][x+dx]
               else:
                  grid[y-dy][x-dx], grid[y][x], grid[y+dy][x+dx] = grid[y+dy][x+dx], grid[y-dy][x-dx], grid[y][x]
            else:
               if grid[y][x] == "[":
                  grid[y][x], grid[y][x+1], grid[y+dy][x], grid[y+dy][x+1] = grid[y+dy][x], grid[y+dy][x+1], grid[y][x], grid[y][x+1]
               else:
                  grid[y][x], grid[y][x-1], grid[y+dy][x], grid[y+dy][x-1] = grid[y+dy][x], grid[y+dy][x-1], grid[y][x], grid[y][x-1]
         elif grid[y][x] == "@":
            grid[y][x], grid[y+dy][x+dx] = grid[y+dy][x+dx], grid[y][x]
         return True
      else:
         return False
   elif grid[y+dy][x+dx] == "#":
      return False
   elif grid[y+dy][x+dx] == ".":
      if grid[y][x] == "@":
         grid[y][x], grid[y+dy][x+dx] = grid[y+dy][x+dx], grid[y][x]
      elif (grid[y][x] == "[" or grid[y][x] == "]") and second == False:
         if dy != 0:
            if grid[y][x] == "[":
               res = next_move(grid, x+1, y, dx, dy, True)
            else:
               res = next_move(grid, x-1, y, dx, dy, True)
            if res:
               if grid[y][x] == "[":
                  grid[y][x], grid[y][x+1], grid[y+dy][x], grid[y+dy][x+1] = grid[y+dy][x], grid[y+dy][x+1], grid[y][x], grid[y][x+1]
               elif grid[y][x] == "]":
                  grid[y][x], grid[y][x-1], grid[y+dy][x], grid[y+dy][x-1] = grid[y+dy][x], grid[y+dy][x-1], grid[y][x], grid[y][x-1]
               return True
            else:
               return False
      return True
   elif grid[y][x] == ".":
      return True
   else:
      return False

def count_boxes(grid):
   sum = 0
   for y, row in enumerate(grid):
      for x, col in enumerate(row):
         if grid[y][x] == "[":
            sum += x + y * 100
   
   return sum


def main():
   with open("input.txt") as f:
      lines = f.read()

   tmp_grid, tmp_movs = lines.split("\n\n")
   grid = [list(row) for row in tmp_grid.split("\n")]

   grid = transform_grid(grid)

   movs = tmp_movs.split("\n")
   x, y = robot_pos(grid)

   for line in movs:
      for mov in line:
         dx, dy = direction[mov]
         res = next_move(grid, x, y, dx, dy, False)
         if res:
            x += dx
            y += dy
   
   sum_boxes = count_boxes(grid)
   #print(grid)
   print(sum_boxes)
   


if __name__ == "__main__":
    main()

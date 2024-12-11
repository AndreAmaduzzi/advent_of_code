"""
6st December, 2024
"""


direction = {
   "<": (-1,0),
   ">": (1,0),
   "^": (0,-1),
   "v": (0,1)
}

next_direction = {
    "<": "^",
    ">": "v",
    "^": ">",
    "v": "<"
}

def search_guard(map):
   for i in range(len(map)):
      for j in range(len(map[0])):
         if map[i][j] == "^":
            guard_pos = (j, i)
            return guard_pos


def check_pos_guards(p_guard, n_rows, n_cols, act_dir):
   dx, dy = direction[act_dir]
   if (p_guard[0] + dx >= n_cols) or (p_guard[0] + dx < 0) or (p_guard[1] + dy >= n_rows) or (p_guard[1] + dy < 0):
      return False
   else:
      return True

def next_iteration(p_guard, act_dir, map):
   dx, dy = direction[act_dir]
   nx, ny = p_guard[0] + dx, p_guard[1] + dy
   while map[ny][nx] == "#":
      act_dir = next_direction[act_dir]
      dx, dy = direction[act_dir]
      nx, ny = p_guard[0] + dx, p_guard[1] + dy
   return (nx, ny), act_dir

def main():
   with open('input.txt') as f:
         lines = f.readlines()

   map = [line.strip() for line in lines]
   
   n_rows = len(map)
   n_cols = len(map[0])

   p_guard = search_guard(map)
   act_dir = "^"

   visited_positions = set()
   visited_positions.add(p_guard)

   while check_pos_guards(p_guard, n_rows, n_cols, act_dir):
      p_guard, act_dir = next_iteration(p_guard, act_dir, map)
      visited_positions.add(p_guard)

   print(len(visited_positions))


if __name__ == "__main__":
    main()

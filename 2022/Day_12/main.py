'''
12st December, 2022
'''

import collections

def get_adjacent(current: (int, int), cols, rows) -> [(int, int)]:
   col, row = current

   match current:
      case (0, 0):
         return [(0, 1), (1, 0)]
      case (0, x):
         return [(col, row - 1), (col + 1, row)] if x == rows - 1 else [(col, row - 1), (col + 1, row),
                                                                         (col, row + 1)]
      case (y, 0):
         return [(col - 1, row), (col, row + 1)] if y == cols - 1 else [(col - 1, row), (col, row + 1),
                                                                         (col + 1, row)]
      case _:
         if current == (cols - 1, rows - 1):
            return [(col, row - 1), (col - 1, row)]
         elif col == cols - 1:
            return [(col, row - 1), (col - 1, row), (col, row + 1)]
         elif row == rows - 1:
            return [(col, row - 1), (col - 1, row), (col + 1, row)]
         else:
            return [(col, row - 1), (col - 1, row), (col, row + 1), (col + 1, row)]


def main():
   with open("input.txt") as f:
      data = [[l for l in line] for line in f.read().strip().split()]

   starting, ending = None, None

   for r, line in enumerate(data):
      if 'S' in line:
         starting = (r, line.index('S'))

      if 'E' in line:
         ending = (r, line.index('E'))

   values = {chr(i): i - 96 for i in range(97, 97 + 26)}
   values['S'] = 1
   values['E'] = 26

   queue, visited = collections.deque(), set()
   queue.append([starting])

   res = 0
   while queue:
      path = queue.popleft()
      row, col = path[-1]
      current_height = values[data[row][col]]

      if (row, col) not in visited:
         visited.add((row, col))

         if (row, col) == ending:
            res = len(path) - 1
            break

         for vertex in get_adjacent((row, col), len(data), len(data[0])):
            vertex_row, vertex_col = vertex
            vertex_height = values[data[vertex_row][vertex_col]]

            if vertex_height <= current_height + 1:
               path_copy = path[:]
               path_copy.append(vertex)
               queue.append(path_copy)

   print(res)

if __name__ == "__main__":
    main()
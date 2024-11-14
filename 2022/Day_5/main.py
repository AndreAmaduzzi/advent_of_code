'''
5st December, 2022
'''

def move(stacks, start, finish, n, type):
   tmp = stacks[start][-n:]
   if (type == 0):
      tmp.reverse()
   stacks[start] = stacks[start][:-n]
   stacks[finish] = stacks[finish] + tmp


def main():

   with open('input.txt', 'r') as f:
      tmp = []
      for line in f:
         if line.strip() == "":
            break
         tmp.append(line.strip("\n"))
      lstacks = [int(i) for i in tmp[-1].split()]
      lstacks.sort()
      stacks = {}
      for k in lstacks:
         stacks[k] = []
      for i in range(len(tmp) - 2, -1, -1):
         boxes = [tmp[i][j : j + 4][1] for j in range(0, len(tmp[i]), 4)]
         for j in range(len(boxes)):
            if boxes[j] != " ":
               stacks[j + 1].append(boxes[j])
      commands = []
      for line in f:
         tmp = line.strip().split()
         commands.append([int(tmp[1]), int(tmp[3]), int(tmp[5])])

   for c in commands:
      move(stacks, c[1], c[2], c[0], 1)

   res = ""
   for k in lstacks:
      res = res + stacks[k][-1]

   print(f"Res: {res}")

if __name__ == "__main__":
    main()
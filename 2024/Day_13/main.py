"""
13st December, 2024
"""


def main():
   with open("input.txt") as f:
      lines = f.read().splitlines()

   ButtonA = [(int(line[12:14]), int(line[18:20])) for i, line in enumerate(lines) if i % 4 == 0]
   ButtonB = [(int(line[12:14]), int(line[18:20])) for i, line in enumerate(lines) if (i-1) % 4 == 0]
   Prizes = [(int(line.split()[1][2:len(line.split()[1]) - 1]), int(line.split()[2][2:])) for i, line in enumerate(lines) if (i-2) % 4 == 0]

   tokens = 0
   tokens2 = 0
   for i in range(len(Prizes)):
      x1, y1 = ButtonA[i]
      x2 , y2 = ButtonB[i]
      c, d = Prizes[i]
      a = (c*y2 - d*x2) / (x1*y2 - y1*x2)
      b = (d*x1 - c*y1) / (x1*y2 - y1*x2)
      if a == int(a) and b == int(b):
         tokens += int(3 * a + b)
      c, d = c + 10000000000000, d + 10000000000000
      a = (c*y2 - d*x2) / (x1*y2 - y1*x2)
      b = (d*x1 - c*y1) / (x1*y2 - y1*x2)
      if a == int(a) and b == int(b):
         tokens2 += int(3 * a + b)

   print(tokens)
   print(tokens2)


if __name__ == "__main__":
    main()

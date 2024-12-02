"""
2st December, 2024
"""

import numpy as np

def check_safe(list):
   
   inc_dec_m1 = np.sign(int(list[1]) - int(list[0]))
   x_m1 = 0
   for x in list:
      x = int(x)
      if x_m1 == 0:
         x_m1 = x
         continue
      
      diff = x - x_m1
      inc_dec = np.sign(diff)
      diff = abs(diff)
      if inc_dec != inc_dec_m1 or diff > 2:
         return False
      
      inc_dec_m1 = inc_dec
      x_m1 = x
   return True

def main():
   with open("test.txt") as f:
       rows = f.readlines()

   levels = []
   for row in rows:
       levels.append(row.strip().split())

   count = 0
   for level in levels:
      if check_safe(level):
         count += 1
   
   print(count)

if __name__ == "__main__":
    main()

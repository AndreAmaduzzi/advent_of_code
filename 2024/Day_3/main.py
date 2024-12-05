"""
3st December, 2024
"""


import re


def clean(s):
    p = re.compile('mul\([0-9]{1,3},[0-9]{1,3}\)')
    result = p.findall(s)
    return result

def mul(s):
    l = list(map(int,s.strip('mul()').split(',')))
    return (l[0] * l[1])


def main():
   with open('input.txt') as f:
         data = f.read()

   total = 0
   for x in clean(data):
         total = total + mul(x)

   print(total)

   partition = re.split('(do\(\)|don\'t\(\))', data)

   total = 0
   do = True
   for s in partition:
      if s == 'do()':
         do = True
      elif s == "don't()":
         do = False
      if (do):
         for x in clean(s):
               total = total + mul(x)

   print(total)

if __name__ == "__main__":
    main()

'''
13st December, 2022
'''

from itertools import zip_longest


def compare(left, right):
    z = zip_longest(left, right, fillvalue=None)

    for p in z:
        l, r = p
        res = None

        if isinstance(l, int) and isinstance(r, int):
            if l < r: return True
            elif l > r: return False
        
        elif isinstance(l, list) and isinstance(r, list):
            res = compare(l, r)
        
        elif isinstance(l, int) and isinstance(r, list):
            res = compare([l], r)
        elif isinstance(l, list) and isinstance(r, int):
            res = compare(l, [r])
        
        # check if one side has run out of items
        elif l == None:
            return True
        elif r == None:
            return False
        
        # return result from any recursive checks
        if res != None: return res


def main():
   with open("input.txt") as f:
      data = f.read().split("\n\n")

   res = 0
   s_pairs = [pair.split("\n") for pair in data]
   pairs = list(map(lambda p: [eval(i) for i in p], s_pairs))

   for i, pair in enumerate(pairs, start=1):
      res += i if compare(pair[0], pair[1]) > 0 else 0
    
   print(res)

if __name__ == "__main__":
    main()
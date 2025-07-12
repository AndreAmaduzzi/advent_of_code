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
      data = f.readlines()

   pairs = [eval(l.strip()) for l in data if l != "\n"]
   sum_two = 1     # add one for 1-indexing
   sum_six = 2     # add one for 1-indexing, another 1 to account for [[2]]
   for p in pairs:
      sum_two += 1 if compare(p, [[2]]) else 0
      sum_six += 1 if compare(p, [[6]]) else 0
    
   print(sum_two * sum_six)

if __name__ == "__main__":
    main()
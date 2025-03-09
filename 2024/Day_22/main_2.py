"""
22st December, 2024
"""


from collections import defaultdict


def calc_secret(num):
   prune_mask = (1 << 24) - 1
   num ^= (num << 6) & prune_mask
   num ^= (num >> 5) 
   num ^= (num << 11) & prune_mask
   return num


def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.readlines()

   secrets = [line.strip() for line in lines]

   total_bananas = defaultdict(int)
   for num in map(int, secrets):
       seen = set()
       diffs = []
       for i in range(2000):
           next_num = calc_secret(num)
           diffs.append((next_num % 10) - (num % 10))
           num = next_num
           if i >= 3:
               if (sequence := tuple(diffs)) not in seen:
                   total_bananas[sequence] += num % 10
                   seen.add(sequence)
               diffs.pop(0)
   
   print(max(total_bananas.values()))


if __name__ == "__main__":
    main()

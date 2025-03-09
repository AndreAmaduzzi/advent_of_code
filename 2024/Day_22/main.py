"""
22st December, 2024
"""


def calc_secret(num, iterations):
   prune_mask = (1 << 24) - 1
   for _ in range(iterations):
      num ^= (num << 6) & prune_mask
      num ^= (num >> 5) 
      num ^= (num << 11) & prune_mask
   return num


def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.readlines()

   secrets = [line.strip() for line in lines]

   sum = 0
   for i in range(len(secrets)):
      sum += calc_secret(int(secrets[i]), 2000)
   
   print(sum)


if __name__ == "__main__":
    main()

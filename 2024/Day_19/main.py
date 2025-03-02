"""
19st December, 2024
"""


def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.read()

   patterns, desired = lines.split("\n\n")

   patterns = patterns.split(", ")
   desired = desired.split("\n")

   def count_matches(i, design):
      if i == len(design): return True
      for towel in patterns:
         if i + len(towel) <= len(design) and design[i:i + len(towel)] == towel and count_matches(i + len(towel), design): return True
      return False

   match_count = sum([1 for design in desired if count_matches(0, design)])
   print(f"Number of matches: {match_count}")


if __name__ == "__main__":
    main()

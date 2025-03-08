"""
21st December, 2024
"""


def main():
   source = "test.txt"
   with open(source) as f:
      lines = f.readlines()

   codes = [line.strip() for line in lines]

   print(codes)

if __name__ == "__main__":
    main()

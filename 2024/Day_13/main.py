"""
13st December, 2024
"""



def main():
   with open("test.txt") as f:
      lines = f.read().splitlines()

   print(lines)


if __name__ == "__main__":
    main()

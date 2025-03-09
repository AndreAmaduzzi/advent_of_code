"""
22st December, 2024
"""


def main():
   source = "test.txt"
   with open(source) as f:
      lines = f.readlines()

   secrets = [line.strip() for line in lines]

   print(secrets)

if __name__ == "__main__":
    main()

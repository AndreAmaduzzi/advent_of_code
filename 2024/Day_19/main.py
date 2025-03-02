"""
19st December, 2024
"""


def main():
   source = "test.txt"
   with open(source) as f:
      lines = f.read()

   patterns, messages = lines.split("\n\n")

   print(patterns)
   print(messages)

if __name__ == "__main__":
    main()

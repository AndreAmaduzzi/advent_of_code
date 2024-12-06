"""
6st December, 2024
"""


direction = {
   "<": (-1,0),
   ">": (1,0),
   "^":_(0,-1),
   "v": (0,1)
}



def search_guard(map):


def main():
   with open('test.txt') as f:
         lines = f.readlines()

   map = [line.strip() for line in lines]
   
   p_guard = search_guard(map)
   
   print(map)



if __name__ == "__main__":
    main()

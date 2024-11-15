'''
6st December, 2022
'''

def check_start_packet(packet):
   tmp = []
   tmp.append(packet[0])
   find = False
   i = 1
   while (find == False):
      if (tmp.find(packet[i]) == -1):
         i = i + 1
         tmp.append(packet[i])

def main():

   with open('test1.txt', 'r') as f:
      line = f.readlines()

   print(line)


if __name__ == "__main__":
    main()
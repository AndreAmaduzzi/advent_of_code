'''
6st December, 2022
'''

def check_start_packet(packet):
   tmp = ''
   tmp = tmp + packet[0]
   find = False
   i = 1
   while ((find == False) and (i < 14)):
      if (tmp.find(packet[i]) == -1):
         tmp = tmp + packet[i]
         i = i + 1
      else: 
         find = True
   return i
   

def main():

   with open('input.txt', 'r') as f:
      line = f.read()

   pattern_match = False
   i = 0
   while ((pattern_match == False) and (line[i + 14] != '\n')):
      res = check_start_packet(line[i : i + 14])
      if (res == 14):
         pattern_match = True
         res_match = i + 14
      else:
         i = i + 1
      
   print(res_match)


if __name__ == "__main__":
    main()
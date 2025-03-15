"""
24st December, 2024
"""

import re
from operator import __and__, __xor__, __or__

def main():
   source = "input.txt"
   with open(source) as f:
      lines = f.read()

   wires, gates = lines.split("\n\n")

   wires_map = {}
   for wire in wires.split("\n"):
      name, value = wire.split(": ")
      wires_map[name] = int(value)

   gates_map = {}
   for in1, op, in2, out in re.findall(r'(\w+) (AND|XOR|OR) (\w+) -> (\w+)', gates):
      gates_map[out] = (op, in1, in2)

   operators = {
       'AND': __and__,
       'XOR': __xor__,
       'OR': __or__
   }
   
   def get_value(wire):
      if wire in wires_map:
          return wires_map[wire]
      op, in1, in2 = gates_map[wire]
      wires_map[wire] = operators[op](get_value(in1), get_value(in2))
      return wires_map[wire]

   max_bit = max(int(wire[1:]) for wire in gates_map if wire.startswith('z'))
   z_bits = [str(get_value(f'z{i:02}')) for i in range(max_bit + 1)]
   print(int(''.join(reversed(z_bits)), 2))

if __name__ == "__main__":
    main()

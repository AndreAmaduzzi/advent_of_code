"""
23st December, 2024
"""


import re
from collections import defaultdict


def main():
   source = "input.txt"
   with open(source) as f:
      links = f.read()

   graph = defaultdict(set)
   for a, b in re.findall(r'(\w+)-(\w+)', links):
       graph[a].add(b)
       graph[b].add(a)

   candidates = [c for c in graph if c.startswith('t')]
   t_triples = set()
   for t in candidates:
       for a in graph[t]:
           for b in graph[a]:
               if b in graph[t]:
                   t_triples.add(tuple(sorted([t, a, b])))
   
   print(len(t_triples))

if __name__ == "__main__":
    main()

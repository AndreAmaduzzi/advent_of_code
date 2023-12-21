"""
20th December, 2023
"""


import sys
from collections import deque
from itertools import count
from math import lcm

def propagate_pulse(graph, flops, conjs, sender, receiver, pulse):
	if receiver in flops:
		if pulse:
			return
		next_pulse = flops[receiver] = not flops[receiver]
	elif receiver in conjs:
		conjs[receiver][sender] = pulse
		next_pulse = not all(conjs[receiver].values())
	elif receiver in graph:
		next_pulse = pulse
	else:
		return

	for new_receiver in graph[receiver]:
		yield receiver, new_receiver, next_pulse

def run(graph, flops, conjs):
	q = deque([('button', 'broadcaster', False)])
	nhi = nlo = 0

	while q:
		sender, receiver, pulse = q.popleft()
		nhi += pulse
		nlo += not pulse
		q.extend(propagate_pulse(graph, flops, conjs, sender, receiver, pulse))

	return nhi, nlo


def main():

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    flops = {}
    conjs = {}
    graph = {}

    for line in lines:
        source, dests = line.split('->')
        source = source.strip()
        dests = dests.strip().split(', ')

        if source[0] == '%':
            source = source[1:]
            flops[source] = False
        elif source[0] == '&':
            source = source[1:]
            conjs[source] = {}

        graph[source] = dests
	
    for source, dests in graph.items():
        for dest in filter(conjs.__contains__, dests):
            conjs[dest][source] = False

    tothi = totlo = 0
    for _ in range(1000):
        nhi, nlo = run(graph, flops, conjs)
        tothi += nhi
        totlo += nlo

    sol = totlo * tothi
    print('Soluzione:')
    print(sol)


if __name__ == "__main__":
    main()
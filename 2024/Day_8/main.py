"""
8st December, 2024
"""


antinodes = set()

def antinode_p1(pr1, pr2, N, M):
    x1, y1 = pr1
    x2, y2 = pr2
    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)
    if newx >= 0 and newx < N and newy >= 0 and newy < M:
        antinodes.add((newx,newy))

def antinode_p2(pr1, pr2, N, M):
    x1, y1 = pr1
    x2, y2 = pr2
    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)
    antinodes.add((x2,y2))
    while newx >= 0 and newx < N and newy >= 0 and newy < M:
        antinodes.add((newx,newy))
        newx += (x2 - x1)
        newy += (y2 - y1)


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    map = [list(line.strip()) for line in lines]
   
    N = len(map)
    M = len(map[0])
    nodes = {}

    for i in range(N):
        for j in range(M):
            if map[i][j] != ".":
                if map[i][j] in nodes:
                    nodes[map[i][j]].append((i,j))
                else:
                    nodes[map[i][j]] = [(i,j)]

    for k in nodes:
        node_list = nodes[k]
        L = len(node_list)
        for i in range(L):
            for j in range(i):
                node1 = node_list[i]
                node2 = node_list[j]
                antinode_p1(node1, node2, N, M)
                antinode_p1(node2, node1, N, M)

    print(len(antinodes))

    antinodes.clear()
    for k in nodes:
        node_list = nodes[k]
        L = len(node_list)
        for i in range(L):
            for j in range(i):
                node1 = node_list[i]
                node2 = node_list[j]
                antinode_p2(node1, node2, N, M)
                antinode_p2(node2, node1, N, M)
    
    print(len(antinodes))


if __name__ == "__main__":
    main()

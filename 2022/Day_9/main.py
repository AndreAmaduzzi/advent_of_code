'''
9st December, 2022
'''

hx, hy = 0, 0
tx, ty = 0, 0

sign = lambda x : 1 if x > 0 else (-1 if x < 0 else 0 )

def update():
    global tx, ty, hx, hy
    dx = tx - hx
    dy = ty - hy
    if dx == 0 or dy == 0:
        if abs(dx) >= 2:
            tx -= sign(dx)
        if abs(dy) >= 2:    
            ty -= sign(dy)
    elif (abs(dx), abs(dy)) != (1, 1):
        tx -= sign(dx)
        ty -= sign(dy)

m = {
    "R" : (1, 0),
    "L" : (-1, 0),
    "U" : (0, 1),
    "D" : (0, -1),
}


def main():
    global tx, ty, hx, hy
    with open("input.txt") as f:
        rows = f.read().strip()
    p = set()
    for x in rows.split("\n"):
        dr, n = x.split(" ")
        n = int(n)
        p.add((tx, ty))
        for _ in range(n):
            dx, dy = m[dr]
            hx += dx
            hy += dy
            update()
            p.add((tx, ty))

    print(len(p))

if __name__ == "__main__":
    main()
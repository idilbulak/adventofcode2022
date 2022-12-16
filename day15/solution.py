with open("input.txt") as file:
    lines = [(int(line.split(" ")[2][2:-1]), int(line.split(" ")[3][2:-1]),
            int(line.split(" ")[8][2:-1]), int(line.split(" ")[9][2:].strip()))
            for line in file]

rst1 = []
for coords in lines:
    dist = abs(coords[0] - coords[2]) + abs(coords[1] - coords[3])
    if 2000000 >= coords[1] - dist and 2000000 <= coords[1] + dist:
        y = (coords[1] - dist + coords[1] + dist) // 2
        dy = abs(2000000 - y)
        rst1.append([coords[0] - dist + dy, coords[0] + dist - dy])
print(max([x[1] for x in rst1]) - min([x[0] for x in rst1]))

rst2 = set((coords[0], coords[1], abs(coords[0] - coords[2]) + abs(coords[1] - coords[3])) for coords in lines)
import sys
for sx, sy, d in rst2:
    for dx in range(d+2):
        dy = d + 1 - dx
        for x, y in [(sx+dx, sy+dy), (sx+dx, sy-dy), (sx-dx, sy+dy), (sx-dx, sy-dy)]:
            if (0<=x<=4_000_000 and 0<=y<=4_000_000) and all(abs(x-sx)+abs(y-sy)>d for sx,sy,d in rst2):
                print(4_000_000 * x + y)

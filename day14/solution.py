with open('input.txt') as file:
    lines = []
    for line in file:
        lines.append(line)

cave = [ ["."] *700 for i in range(700)]
for line in lines:
    line = line.strip()
    # add rocks
    coordinates = line.split('->')
    end = None
    for coordinate in coordinates:
        coord = tuple(map(int, coordinate.strip().split(',')))            
        if end is not None:
            # draw path
            c1 = coord
            c2 = end
            if coord[0] > end[0] or coord[1] > end[1]:
                c1 = end
                c2 = coord
            x = c1[0]
            y = c1[1]
            if c1[0] == c2[0]:
                while y <= c2[1]:
                    cave[y][x] = "#"
                    y += 1
            else:
                while x <= c2[0]:
                    cave[y][x] = "#"
                    x += 1 
        end = coord

def sand(cave, drop_coord):
    rest_coord = None
    curr = (drop_coord[0], drop_coord[1])
    while True:
        if curr[1] + 1 >= len(cave):
            return None
        if cave[curr[1] + 1][curr[0]] == ".":
            curr = (curr[0], curr[1] + 1)
        elif cave[curr[1] + 1][curr[0] - 1] == ".":
            curr = (curr[0] - 1, curr[1] + 1)
        elif cave[curr[1] + 1][curr[0] + 1] == ".":
            curr = (curr[0] + 1, curr[1] + 1)
        else:
            rest_coord = curr
            cave[curr[1]][curr[0]] = "O"
            break
    return rest_coord

rested_sand = 0
coord = sand(cave, (500,0))
while coord is not None:
    rested_sand += 1
    coord = sand(cave, (500,0))
print(rested_sand)

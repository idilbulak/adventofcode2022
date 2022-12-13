class rope:
    def __init__(val, x, y):
        val.x = x
        val.y = y

def move(H,T):
    if(abs(H.y - T.y) == 1 and abs(H.x - T.x) == 1):
        pass
    elif(H.y - T.y == 2 and H.x - T.x == -1):
        T.y += 1
        T.x -= 1
    elif(H.y - T.y == 2 and H.x - T.x == 1):
        T.y += 1
        T.x += 1
    elif(H.y - T.y == -2 and H.x - T.x == -1):
        T.y -= 1
        T.x -= 1
    elif(H.y - T.y == -2 and H.x - T.x == 1):
        T.y -= 1
        T.x += 1
    elif(H.y - T.y == -1 and H.x - T.x == 2):
        T.y -= 1
        T.x += 1
    elif(H.y - T.y == 1 and H.x - T.x == 2):
        T.y += 1
        T.x += 1
    elif(H.y - T.y == -1 and H.x - T.x == -2):
        T.y -= 1
        T.x -= 1
    elif(H.y - T.y == 1 and H.x - T.x == -2):
        T.y += 1
        T.x -= 1
    else:
        if(H.y - T.y > 1):
            T.y += 1
        if(T.y - H.y > 1):
            T.y -= 1
        if(H.x - T.x > 1):
            T.x += 1
        if(T.x - H.x > 1):
            T.x -= 1


with open('input.txt') as file:
    lines = []
    for line in file:
        lines.append(line.strip())

    H = rope(0,0)
    T = rope(0,0)
    rp_arr = [rope(0,0) for i in range(9)]

    coord = []
    coord2 = []

    for row in lines:
        direction = row.split(' ')[0]
        distance = int(row.split(' ')[1])
        for _ in range(distance, 0, -1):
            if direction == 'U':
                H.y += 1
            elif direction == 'D':
                H.y -= 1
            elif direction == 'R':
                H.x += 1
            elif direction == 'L':
                H.x -= 1

            move(H,T)
            if ([T.x, T.y] not in coord):
                coord.append([T.x, T.y])

            for i, num in enumerate(rp_arr):

                if(i == 0):
                    num = move(H, num)
                else:
                    num = move(rp_arr[i - 1], num)
   
            if ([rp_arr[8].x, rp_arr[8].y] not in coord2):
                coord2.append([rp_arr[8].x, rp_arr[8].y])

print(len(coord))
print(len(coord2))

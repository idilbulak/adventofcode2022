import math
with open('input.txt') as file:
    lines = []
    for line in file:
        lines.append(line.strip())

mx = []
mx = [[int(x) for x in line] for line in lines]

visible_trees = set()
for i in range(len(mx)):
    for j in range(len(mx[0])):
        if_taller = [True,True,True,True]
        for x in range(j + 1, len(mx[0])):
            if mx[i][x] >= mx[i][j]:
                if_taller[0] = False
                break
        for x in range(0, j):
            if mx[i][x] >= mx[i][j]:
                if_taller[1] = False
                break
        for x in range(i + 1, len(mx)):
            if mx[x][j] >= mx[i][j]:
                if_taller[2] = False
                break
        for x in range(0, i):
            if mx[x][j] >= mx[i][j]:
                if_taller[3] = False
                break
        if True in if_taller:
            visible_trees.add((i, j))

p1 = print(len(visible_trees))

scores = set()
for i in range(len(mx)):
    for j in range(len(mx[0])):
        score = [0,0,0,0]
        for k in range(1, i + 1):
            score[0] += 1
            if mx[i - k][j] >= mx[i][j]:
                break
        for k in range(i + 1, len(mx)):
            score[1] += 1
            if mx[k][j] >= mx[i][j]:
                break
        for k in range(1, j + 1):
            score[2] += 1
            if mx[i][j - k] >= mx[i][j]:
                break
        for k in range(j + 1, len(mx[0])):
            score[3] += 1
            if mx[i][k] >= mx[i][j]:
                break
        scores.add(math.prod(score))

p2 = print(max(scores))

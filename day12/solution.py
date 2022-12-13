# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
# https://www.youtube.com/watch?v=KiCBXu4P-2Y

from collections import defaultdict, deque
with open('input.txt') as file:
    mx = []
    i = 0
    for line in file:
        mx.append([ord(x) for x in list(line.strip())])
        for j in range(len(list(line.strip()))):
            if list(line.strip())[j] == 'S':
                start = tuple([i,j])
                mx[i][j] = ord('a')
            if list(line.strip())[j] == 'E':
                goal = tuple([i,j])
                mx[i][j] = ord('z')
        i += 1

explored = defaultdict()
explored[start] = 0
queue = deque()
queue.append(start)
while (queue):
    neighbors = []
    node = queue.popleft()
    if node[0] - 1 >= 0 and mx[node[0] - 1][node[1]] <= (mx[node[0]][node[1]] + 1):
        neighbors.append(tuple([node[0] - 1,node[1]]))
    if node[0] + 1 < len(mx) and mx[node[0] + 1][node[1]] <= (mx[node[0]][node[1]] + 1):
        neighbors.append(tuple([node[0] + 1,node[1]]))
    if node[1] - 1 >= 0 and mx[node[0]][node[1] - 1] <= (mx[node[0]][node[1]] + 1):
        neighbors.append(tuple([node[0],node[1] - 1]))
    if node[1] + 1 < len(mx[0]) and mx[node[0]][node[1] + 1] <= (mx[node[0]][node[1]] + 1):
        neighbors.append(tuple([node[0],node[1] + 1]))
    for neighbor in neighbors:
        if neighbor not in explored:
            explored[neighbor] = explored[node] + 1
            queue.append(neighbor)
print(explored[goal])

possible_starts = []
for i in range(len(mx)):
    for j in range(len(mx[0])):
        if mx[i][j] == ord('a'):
            possible_starts.append(tuple([i,j]))
min_steps = len(mx) * len(mx[0])
for x in possible_starts:
    explored = defaultdict()
    explored[x] = 0
    queue = deque()
    queue.append(x)
    while (queue):
        neighbors = []
        node = queue.popleft()
        if node[0] - 1 >= 0 and mx[node[0] - 1][node[1]] <= (mx[node[0]][node[1]] + 1):
            neighbors.append(tuple([node[0] - 1,node[1]]))
        if node[0] + 1 < len(mx) and mx[node[0] + 1][node[1]] <= (mx[node[0]][node[1]] + 1):
            neighbors.append(tuple([node[0] + 1,node[1]]))
        if node[1] - 1 >= 0 and mx[node[0]][node[1] - 1] <= (mx[node[0]][node[1]] + 1):
            neighbors.append(tuple([node[0],node[1] - 1]))
        if node[1] + 1 < len(mx[0]) and mx[node[0]][node[1] + 1] <= (mx[node[0]][node[1]] + 1):
            neighbors.append(tuple([node[0],node[1] + 1]))
        for neighbor in neighbors:
            if neighbor not in explored:
                explored[neighbor] = explored[node] + 1
                queue.append(neighbor)
    if goal in explored.keys():
        steps =  explored[goal]
    min_steps = min(min_steps,steps)
print(min_steps)



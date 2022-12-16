with open ("input.txt", "r") as file:
    data = file.read().strip().split("\n")

cycles = [20, 60, 100, 140, 180, 220]
queue = []
register = 1
total = 0
for i in range(len(data)):
    queue.append(0)
    if "addx" in data[i]:
        change = int(data[i].split(" ")[1])
        queue.append(change)
for cycle in range(1, len(queue) + 1):
    if cycle in cycles:
        total += register * cycle
    register += queue.pop(0)      
print (total)


queue = []
register = 1
for i in range(len(data)):
    if "addx" in data[i]:
        change = int(data[i].split(" ")[1])
        queue.append(0)
        queue.append(change)
    if "noop" in data[i]:
        queue.append(0)
sprite = 1
row = -1
line = ""
board = []
for cycle in range(1, len(queue) + 1):
    if (cycle - 1) % 40 == 0:
        row += 1
        if row != 0:
            board.append(line)
            line = ""
    index = cycle - (40 * row) - 1
    if index >= sprite - 1 and index <= sprite + 1:
        line += "#"
    else:
        line += "."
    register += queue.pop(0)
    sprite = register
board.append(line)
for i in board:
    open("result.txt", "a").write(i + '\n')

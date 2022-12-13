with open('input.txt') as file:
    lines = []
    for line in file:
        lines.append(line.strip())

stacks1 = {}
stacks2 = {}
for i in range(0,9):
 stacks1[i+1] = []
 stacks2[i+1] = []

for i in range(7, -1, -1):
 line = lines[i]
 for j,k in enumerate(range(1,len(line),4)):
  if (line[k] != " "):
   stacks1[j+1].append(line[k])
   stacks2[j+1].append(line[k])

for i in range(10, len(lines)):
 instruction = lines[i].split(" ")
 amount = int(instruction[1])
 src = int(instruction[3])
 dest = int(instruction[5])
 for _ in range(amount):
  stacks1[dest].append(stacks1[src].pop())
 stacks2[dest].extend(stacks2[src][-1 * amount:])
 stacks2[src] = stacks2[src][:-1 * amount]

rst1 = ""
rst2 = ""
for i in range(len(stacks1)):
 if (len(stacks1[i+1]) > 0):
  rst1 += stacks1[i+1][-1]
  rst2 += stacks2[i+1][-1]
 
print(rst1, rst2)

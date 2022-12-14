import ast

def compare(left,right):
    if isinstance(left, int) and isinstance(right,int):
        if left < right:
            return 1
        elif left != right:
            return -1
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(0,min(len(left), len(right))):
            if compare(left[i], right[i]):
                return compare(left[i], right[i])
        if min(len(left), len(right))==len(left) and min(len(left), len(right))<len(right):
            return 1
        elif min(len(left), len(right))==len(right) and min(len(left), len(right))<len(left):
            return -1
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    

with open('input.txt') as file:
    lines = []
    for line in file:
        lines.append(line.strip())

pairs = []
pair = 0
for x in range (0,len(lines),3):
    pair += 1
    left = ast.literal_eval(lines[x])
    right = ast.literal_eval(lines[x+1])
    if compare(left,right) == 1:
        pairs.append(pair)    
print(sum(pairs))


with open('input.txt') as file:
    lines = []
    for line in file:
        if line != "\n":
            lines.append(line.strip())
lines.append("[[2]]")
lines.append("[[6]]")

packets = []
for x in range (0,len(lines)):
    packets.append(ast.literal_eval(lines[x]))

for i in range(len(packets)):
    for j in range(len(packets)-i-1):
        if compare(packets[j], packets[j+1]) == -1:
            packets[j], packets[j+1] = packets[j+1], packets[j]

index1 = 0
index2 = 0
for i in range(len(packets)):
    if packets[i] == [[2]]:
        index1 = i+1
    if packets[i] == [[6]]:
        index2 = i+1
print(index1*index2)
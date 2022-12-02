with open('guide.txt') as file:
    list = []
    for line in file:
        list.append(line.strip())

p1 = 0
p2 = 0
for x in list:
    a = x[0]
    b = x[2]
    if a == 'A' and b == 'X':
        p1 += 4
        p2 += 3
    if a == 'A' and b == 'Y':
        p1 += 8 
        p2 += 4
    if a == 'A' and b == 'Z':
        p1 += 3 
        p2 += 8 
    if a == 'B' and b == 'X':
        p1 += 1 
        p2 += 1 
    if a == 'B' and b == 'Y':
        p1 += 5 
        p2 += 5 
    if a == 'B' and b == 'Z':
        p1 += 9 
        p2 += 9 
    if a == 'C' and b == 'X':
        p1 += 7
        p2 += 2
    if a == 'C' and b == 'Y':
        p1 += 2 
        p2 += 6 
    if a == 'C' and b == 'Z':
        p1 += 6 
        p2 += 7
print(p1, p2)

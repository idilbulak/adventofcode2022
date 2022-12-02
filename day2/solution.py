with open('guide.txt') as file:
    list = []
    for line in file:
        list.append(line.strip())

point = 0
for x in list:
    a = x[0]
    b = x[2]
    if a == 'A' and b == 'X':
        point += 4 
    if a == 'A' and b == 'Y':
        point += 8 
    if a == 'A' and b == 'Z':
        point += 3 
    if a == 'B' and b == 'X':
        point += 1 
    if a == 'B' and b == 'Y':
        point += 5 
    if a == 'B' and b == 'Z':
        point += 9 
    if a == 'C' and b == 'X':
        point += 7
    if a == 'C' and b == 'Y':
        point += 2 
    if a == 'C' and b == 'Z':
        point += 6 
print(point)

point = 0
for x in list:
    a = x[0]
    b = x[2]
    if a == 'A' and b == 'X':
        point += 3 
    if a == 'A' and b == 'Y':
        point += 4 
    if a == 'A' and b == 'Z':
        point += 8 
    if a == 'B' and b == 'X':
        point += 1 
    if a == 'B' and b == 'Y':
        point += 5 
    if a == 'B' and b == 'Z':
        point += 9 
    if a == 'C' and b == 'X':
        point += 2
    if a == 'C' and b == 'Y':
        point += 6 
    if a == 'C' and b == 'Z':
        point += 7 
print(point)
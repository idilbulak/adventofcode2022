with open('guide.txt') as file:
    list = []
    for line in file:
        list.append(line.strip())

p1 = 0
p2 = 0
for x in list:
    if x == "A X":
        p1 += 4
        p2 += 3
    if x == "A Y":
        p1 += 8 
        p2 += 4
    if x == "A Z":
        p1 += 3 
        p2 += 8 
    if x == "B X":
        p1 += 1 
        p2 += 1 
    if x == "B Y":
        p1 += 5 
        p2 += 5 
    if x == "B Z":
        p1 += 9 
        p2 += 9 
    if x == "C X":
        p1 += 7
        p2 += 2
    if x == "C Y":
        p1 += 2 
        p2 += 6 
    if x == "C Z":
        p1 += 6 
        p2 += 7
print(p1, p2)

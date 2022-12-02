with open('guide.txt') as file:
    list = []
    for line in file:
        list.append(line.strip())

points=[]
p1 = 0
p2 = 0
dict = {
    "A X": [4, 3],
    "A Y": [8, 4],
    "A Z": [3, 8],
    "B X": [1, 1],
    "B Y": [5, 5],
    "B Z": [9, 9],
    "C X": [7, 2],
    "C Y": [2, 6],
    "C Z": [6, 7]
}

for x in list:
    points += dict[x]
for i in range(0, len(points)):
    if not i % 2:
        p1 += points[i]
    else:
        p2 += points[i]
print(p1, p2)

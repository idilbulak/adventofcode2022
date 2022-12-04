with open('input.txt') as file:
    list = []
    for line in file:
        list.append(line.strip())

count1 = 0
count2 = 0
for line in list:
    set1 = set()
    set2 = set()
    r1, r2 = line.split(',')
    first1, last1 = r1.split('-')
    first2, last2 = r2.split('-')
    for x in range(int(first1), int(last1)+1):
        set1.add(x)
    for y in range(int(first2), int(last2)+1):
        set2.add(y)
    if set2.issubset(set1) or set1.issubset(set2):
        count1 += 1
    if set1 & set2 != set():
        count2 += 1
print (count1, count2)

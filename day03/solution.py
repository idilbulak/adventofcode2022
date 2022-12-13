with open('input.txt') as file:
    list = []
    for line in file:
        list.append(line.strip())

priority = 0
for x in list:
    c1 = x[:len(x)//2]
    c2 = x[len(x)//2:]
    item = set(c1).intersection(set(c2))
    for y in item:
        diff = (ord('A')-27) if y.isupper() else (ord('a')-1)
        priority += ord(y) - diff
print(priority)

priority = 0
for i in range(0, len(list), 3):
    e1 = list[i]
    e2 = list[i+1]
    e3 = list[i+2]
    item = set(e1).intersection(set(e2))
    item = set(item).intersection(set(e3))
    for y in item:
        diff = (ord('A')-27) if y.isupper() else (ord('a')-1)
        priority += ord(y) - diff
print(priority)

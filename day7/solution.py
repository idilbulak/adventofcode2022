from collections import defaultdict

mydict = defaultdict(int)
path = []

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        words = line.split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        else:
            if words[0] == 'dir':
                continue
            else:
                size = int(words[0])
                for i in range(len(path)+1):
                    mydict['/'.join(path[:i])] += size

res1 = 0
for key in mydict:
    if mydict[key] <= 100000:
        res1 += mydict[key]
print(res1)

to_del = mydict['/'] - 40000000
res2 = 70000000
for key in mydict:
    if mydict[key] >= to_del:
        res2 = min(res2, mydict[key])
print(res2)

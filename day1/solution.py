with open('input.txt') as file:
    list = []
    for line in file:
        list.append(line.strip())

c = []
new_list = (' '.join(list)).split('  ')
for x in new_list:
    totc = 0
    for y in x.split(' '):
        totc += int(y)
    c.append(totc)

c.sort(reverse=True)
print(c[0], sum(c[:3]))

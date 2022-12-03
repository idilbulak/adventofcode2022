with open('input.txt') as file:
    list = []
    for line in file:
        list.append(line.strip())

calories = []
elves = (' '.join(list)).split('  ')
for elf in elves:
    totalcal = 0
    for x in elf.split(' '):
        totalcal += int(x)
    calories.append(totalcal)

calories.sort(reverse=True)
print(max(calories), sum(calories[:3]))

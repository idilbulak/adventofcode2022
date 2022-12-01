list = [l.strip() for l in open('calories.txt')]
calories = []


for elf in ('\n'.join(list)).split('\n\n'):
    totalcal = 0
    for x in elf.split('\n'):
        totalcal += int(x)
    calories.append(totalcal)

print(max(calories))

calories.sort()
calories.reverse()

print(sum(calories[:3]))

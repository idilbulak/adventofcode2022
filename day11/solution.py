monkeys = [[98, 97, 98, 55, 56, 72], [73, 99, 55, 54, 88, 50, 55], 
        [67, 98], [82, 91, 92, 53, 99], [52, 62, 94, 96, 52, 87, 53, 60],
        [94, 80, 84, 79], [89], [70, 59, 63]]

inspection = [0,0,0,0,0,0,0,0]

for _ in range(0,20):
        inspection[0] += len(monkeys[0])
        for _ in range(0,len(monkeys[0])):
            rst = (monkeys[0][0] * 13) // 3
            if rst % 11 == 0:
                monkeys[4].append(rst)
            else:
                monkeys[7].append(rst)
            monkeys[0].pop(0)
        inspection[1] += len(monkeys[1])
        for _ in range(0,len(monkeys[1])):
            rst = (monkeys[1][0] + 4) // 3
            if rst % 17 == 0:
                monkeys[2].append(rst)
            else:
                monkeys[6].append(rst)
            monkeys[1].pop(0)
        inspection[2] += len(monkeys[2])
        for _ in range(0,len(monkeys[2])):
            rst = (monkeys[2][0] * 11) // 3
            if rst % 5 == 0:
                monkeys[6].append(rst)
            else:
                monkeys[5].append(rst)
            monkeys[2].pop(0)
        inspection[3] += len(monkeys[3])
        for _ in range(0,len(monkeys[3])):
            rst = (monkeys[3][0] + 8) // 3
            if rst % 13 == 0:
                monkeys[1].append(rst)
            else:
                monkeys[2].append(rst)
            monkeys[3].pop(0)
        inspection[4] += len(monkeys[4])
        for _ in range(0,len(monkeys[4])):
            rst = (monkeys[4][0] * monkeys[4][0]) // 3
            if rst % 19 == 0:
                monkeys[3].append(rst)
            else:
                monkeys[1].append(rst)
            monkeys[4].pop(0)
        inspection[5] += len(monkeys[5])
        for _ in range(0,len(monkeys[5])):
            rst = (monkeys[5][0] + 5) // 3
            if rst % 2 == 0:
                monkeys[7].append(rst)
            else:
                monkeys[0].append(rst)
            monkeys[5].pop(0)
        inspection[6] += len(monkeys[6])
        for _ in range(0,len(monkeys[6])):
            rst = (monkeys[6][0] + 1) // 3
            if rst % 3 == 0:
                monkeys[0].append(rst)
            else:
                monkeys[5].append(rst)
            monkeys[6].pop(0)
        inspection[7] += len(monkeys[7])
        for _ in range(0,len(monkeys[7])):
            rst = (monkeys[7][0] + 3) // 3
            if rst % 7 == 0:
                monkeys[4].append(rst)
            else:
                monkeys[3].append(rst)
            monkeys[7].pop(0)
    

max1 = max(inspection)
inspection.remove(max1)
max2 = max(inspection)
print(max1*max2)

monkeys = [[98, 97, 98, 55, 56, 72], [73, 99, 55, 54, 88, 50, 55], 
        [67, 98], [82, 91, 92, 53, 99], [52, 62, 94, 96, 52, 87, 53, 60],
        [94, 80, 84, 79], [89], [70, 59, 63]]

inspection = [0,0,0,0,0,0,0,0]

mods = 11 * 17 * 5 * 13 * 19 * 2 * 3 * 7

for _ in range(0,10000):
        inspection[0] += len(monkeys[0])
        for _ in range(0,len(monkeys[0])):
            rst = (monkeys[0][0] * 13) % mods
            if rst % 11 == 0:
                monkeys[4].append(rst)
            else:
                monkeys[7].append(rst)
            monkeys[0].pop(0)
        inspection[1] += len(monkeys[1])
        for _ in range(0,len(monkeys[1])):
            rst = (monkeys[1][0] + 4) % mods
            if rst % 17 == 0:
                monkeys[2].append(rst)
            else:
                monkeys[6].append(rst)
            monkeys[1].pop(0)
        inspection[2] += len(monkeys[2])
        for _ in range(0,len(monkeys[2])):
            rst = (monkeys[2][0] * 11) % mods
            if rst % 5 == 0:
                monkeys[6].append(rst)
            else:
                monkeys[5].append(rst)
            monkeys[2].pop(0)
        inspection[3] += len(monkeys[3])
        for _ in range(0,len(monkeys[3])):
            rst = (monkeys[3][0] + 8) % mods
            if rst % 13 == 0:
                monkeys[1].append(rst)
            else:
                monkeys[2].append(rst)
            monkeys[3].pop(0)
        inspection[4] += len(monkeys[4])
        for _ in range(0,len(monkeys[4])):
            rst = (monkeys[4][0] * monkeys[4][0]) % mods
            if rst % 19 == 0:
                monkeys[3].append(rst)
            else:
                monkeys[1].append(rst)
            monkeys[4].pop(0)
        inspection[5] += len(monkeys[5])
        for _ in range(0,len(monkeys[5])):
            rst = (monkeys[5][0] + 5) % mods
            if rst % 2 == 0:
                monkeys[7].append(rst)
            else:
                monkeys[0].append(rst)
            monkeys[5].pop(0)
        inspection[6] += len(monkeys[6])
        for _ in range(0,len(monkeys[6])):
            rst = (monkeys[6][0] + 1) % mods
            if rst % 3 == 0:
                monkeys[0].append(rst)
            else:
                monkeys[5].append(rst)
            monkeys[6].pop(0)
        inspection[7] += len(monkeys[7])
        for _ in range(0,len(monkeys[7])):
            rst = (monkeys[7][0] + 3) % mods
            if rst % 7 == 0:
                monkeys[4].append(rst)
            else:
                monkeys[3].append(rst)
            monkeys[7].pop(0)
    

max1 = max(inspection)
inspection.remove(max1)
max2 = max(inspection)
print(max1*max2)

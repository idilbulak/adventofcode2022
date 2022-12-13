with open('input.txt') as file:
    line = file.readline()

for i in range(len(line)):
    packet = line[i:i + 4]
    packet_len = len(set(packet))
    if packet_len == 4:
        index = line.index(packet)
        print(index + 4)
        break

for i in range(len(line)):
    packet = line[i:i + 14]
    packet_len = len(set(packet))
    if packet_len == 14:
        index = line.index(packet)
        print(index + 14)
        break
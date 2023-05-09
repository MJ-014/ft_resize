from re import search
from sys import argv

inp = open(argv[1], 'r')
oup = open(argv[1].replace('.txt', '_resize.txt'), 'a')
number = int(argv[2])
x = inp.read().replace('TRACK 256', f'TRACK {number + 1}')
x = x.split('\n')

for i in x:
    if 'PATTERN' in i:
        x.pop(x.index(i) - 1)
        x.remove(i)

x = '\n'.join(x)

n = search('ROW', x).start()
part2 = x[n:]

part2 = part2.split('\n')

count1 = 0
for i in range(len(part2)):
    if 'ROW' in part2[i]:
        if count1 > number:
            count1 = 0
        if count1 < 16:
            part2[i] = part2[i][:4] + '0' + hex(count1)[2:].upper() + part2[i][6:]
        else:
            part2[i] = part2[i][:4] + hex(count1)[2:].upper() + part2[i][6:]
        count1 += 1

count2 = 0
count3 = 0
while count2 < len(part2):
    if 'ROW 00' in part2[count2]:
        part2.insert(count2, f'\nPATTERN 0{hex(count3)[2:].upper()}')
        count2 += 1
        count3 += 1
    count2 += 1

part2 = '\n'.join(part2)

oup.write(x[:n] + part2)

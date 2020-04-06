def count_things(purchase):
    info = {}
    for j in purchase:
        if j[0] in info:
            sup = info.get(j[0])
            info[j[0]] = int(sup) + int(j[1])
        else:
            info[j[0]] = j[1]
    
    return sorted(info.items())

fin = open ('input.txt', 'r')
fout = open('output.txt', 'w')

purchase = {}
custom = {}
for i in fin:
    buyer, thing, count = i.split()
    if buyer in purchase:
        purchase[buyer].append((thing, count))
    else:
        purchase[buyer] =[(thing, count)]

for i in sorted(purchase):
    fout.write(i + ':' + '\n')
    for th, c in count_things(purchase[i]):
        fout.write(th + ' ' + str(c) + '\n')

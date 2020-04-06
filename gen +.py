fin = open ('input.txt', 'r')

n = int(fin.readline())
gen = {}
dictionary = {}
for i in fin:
    child, parent = i.split()
    dictionary[child] = 0
    dictionary[parent] = 0
    if parent not in gen:
        gen[parent] = 0
    gen[child] = parent

for i in gen:
    count = 0
    first_i = i
    while gen[i]:
        i = gen[i]
        count = count + 1
    dictionary[first_i] = count

for i, j in sorted(dictionary.items()):
    print(i, j)
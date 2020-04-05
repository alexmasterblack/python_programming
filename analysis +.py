fin = open('input.txt')

string = fin.read().split()

dictionary = {}
for i in string:
    if i in dictionary:
        last_value = dictionary.get(i)
        dictionary[i] = last_value + 1
    else:
        dictionary[i] = 1

sorted_dict = sorted(dictionary.items(), key = lambda i: -i[1])

equal = [[] for i in range(sorted_dict[0][1])]

for i in range(len(sorted_dict)):
    equal[-sorted_dict[i][1]].append(sorted_dict[i][0])

for i in equal:
    i.sort()
    for j in i:
        print(j)

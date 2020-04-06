n = int(input())

string = {}
for i in range(n): 
    word, *transl = input().replace(',', '').split()
    del transl[0]
    for j in transl:
        if j not in string.keys():
            string[j] = []
        string[j].append(word)


print(len(list(string.keys())))

sorted_string = sorted(string.items())

for i, j in sorted_string:
    elem = str(j).replace('[', '').replace(']', '').replace('\'', '')
    print(i, '-', elem)

n, m, k = input().split()
table = [[0 for i in range(int(m) + 2)] for j in range(int(n) + 2)]
for i in range(int(k)):
        line, column = input().split()
        table[int(line)][int(column)] = '*'
        for j in range(int(line) - 1, int(line) + 2):
                for l in range(int(column) - 1, int(column) + 2):
                        if table[j][l] != '*':
                                table[j][l] = table[j][l] + 1

for i in table[1:int(n) + 1]:
    print(' '.join([str(j) for j in i[1:int(m)+1]]))  
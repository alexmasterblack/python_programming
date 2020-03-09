def transpose(table, n, m):
    table = [[table[i][j] for i in range(int(n))] for j in range(int(m))]
    for i in table:
        print(' '.join([str(j) for j in i]))

n, m = input().split()
transpose([[int(i) for i in input().split()] for j in range(int(n))], n, m)
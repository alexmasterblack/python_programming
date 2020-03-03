n = [int(i) for i in input().split()]
bowls = [str(i) for i in range(1, n[0] + 1)]

for i in range (1, n[1] + 1):
    k = [int(j) for j in input().split()]
    shoot = [str(j) for j in range(k[0], k[1] + 1)]
    for j in range(len(bowls)):
        for l in range(len(shoot)):
            if shoot[l] == bowls[j]:
                bowls[j] = '.'
for j in range(len(bowls)):
    if bowls[j] != '.':
        bowls[j] = 'I'

print(''.join(bowls))
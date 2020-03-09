n, k = input().split()
bowls = [str(i) for i in range(1, int(n)+1)]

for i in range (int(k)):
    k_1, k_2 = input().split()
    shoot = [str(j) for j in range(int(k_1), int(k_2) + 1)]
    for j in range(len(bowls)):
        for l in range(len(shoot)):
            if shoot[l] == bowls[j]:
                bowls[j] = '.'
for j in range(len(bowls)):
    if bowls[j] != '.':
        bowls[j] = 'I'

print(''.join(bowls))

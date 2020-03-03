word = ''.join([str(n)for n in input().split()])
print('YES' if word == word[::-1] else 'NO')
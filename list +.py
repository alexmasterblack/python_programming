def rec(n , line):
    if n > 0:
        return rec(n - 2, [line] * 2)
    return line

n = int(input())
line = [0, 0]
if n == 1:
    print(line)
else:
    print(rec(n, line))

#spisok = [[[0, 0]]*2]*2
#print(spisok)
fout = open('output.txt', 'w')

n = int(input())

file_name = {}
for i in range(n):
    name, *value = input().split()
    file_name[name] = value

m = int(input())

for i in range(m):
    act, new_name = input().split()
    values = file_name.get(new_name)
    if act == 'write':
        act = 'W'
    elif act == 'read':
        act = 'R'
    elif act == 'execute':
        act = 'X'
    if act in values:
        fout.write('OK' + '\n')
    else:
        fout.write('Access denied' + '\n')

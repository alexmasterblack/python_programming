n = int(input())
line = [int(i) for i in input().split()]
petya = int(input())
line = [int (i) for i in range(n) if petya <= line[i]]
print(len(line) + 1)
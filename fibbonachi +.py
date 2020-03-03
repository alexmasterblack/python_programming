n = int(input())
fib = [0, 1]

for i in range(1, n+1):
    print(fib[i], end =' ')
    fib.append(fib[i]+fib[i-1])
n = int(input())
shift = [int(i) for i in input().split()]
k = int(input())

print(*(shift[-1 * (k % n):] + shift[:-1 * (k % n)] if k >= 0 else shift[-k % n:] + shift[:-k % n]))
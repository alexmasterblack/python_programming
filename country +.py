fout = open('output.txt', 'w')

n = int(input())

cities = {}
for i in range(n):
    country, *city = input().split()
    for i in city:
        cities[i] = country

m = int(input())

for i in range(m):
    new_city = input()
    fout.write(cities[new_city] + '\n')
fin = open('input.txt')

line = fin.read().splitlines()

print(*sorted(line, key=lambda i: (sum([ord(letter) - ord('A') for letter in i.upper()]), i)), sep ='\n')
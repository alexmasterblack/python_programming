import math

def prime_num(number):
    elem = 2
    while number % elem != 0:
        elem += 1
    if elem == number:
        return True
    else:
        return False

def palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def power(number):
    if math.sqrt(number) % 2 == 0:
        return True
    elif math.sqrt(number) % 2 != 0:
        return False

def check_pin(a, b, c):
    return prime_num(a) and palindrome(b) and power(c)

a, b, c = map(int, input().split('-'))

if check_pin(a, b, c):
    print('Корректен')
else:
    print('Некорректен')

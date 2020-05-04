def password_level(letter):
    if len(letter) < 6:
        print('Недопустимый пароль')
    elif letter.isdigit() or (letter.isalpha() and letter.islower()) or (letter.isalpha() and letter.isupper()):
        print('Ненадежный пароль')
    elif letter.isalpha() or (letter.isalnum() and letter.islower()) or (letter.isalnum() and letter.isupper()):
        print('Слабый пароль')
    else:
        print('Надежный пароль')

password = input()
password_level(password)
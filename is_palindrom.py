def is_palindrom(str):
    reversed_str=''.join(reversed(str))
    if reversed_str==str:
        return True
    else:
        return False

string=input('Введите строку(все символы должны находиться в нижнем регистре и без пробелов): ')

print(is_palindrom(string))



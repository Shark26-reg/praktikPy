"""Задание 5. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж"""

text = input("Введите слова через пробел: ")
lst = text.split()
for x, y in enumerate (lst, start = 1):
    if len(y) > 11:
        y = y[:10]
        print(x, y)
    else :
        print (x, y)
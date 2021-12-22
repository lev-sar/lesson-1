# Задание 1-1.b

# my_num = {'One': 'один',
#     'two': 'два',
#     'three': 'три',
#     'four': 'четыре',
#     'Five': 'пять',
#     'six': 'шесть',
#     'seven': 'семь',
#     'eight': 'восемь',
#     'nine': 'девять',
#     'ten': 'десять'}
#
# def num_translate():
#     number = input('Введите число')
#     if number.istitle():
#         print(my_num.get(number.lower()).title())
#     else:
#         print(my_num.get(number))
#
#
# num_translate()

# Задание 3

# names = ('Мария', 'Иван', 'Стас', 'Игорь', 'Пётр', 'Аркадий')
#
# def thesaurus(*names):
#     res = {}
#     for name in names:
#         key = name[0].capitalize()
#         if key not in res:
#             res[key] = []
#         res[key].append(name)
#     return res
#
# print(thesaurus('Мария', 'Иван', 'Стас', 'Игорь', 'Пётр', 'Аркадий' ))


# Задание 5__________________________________________

from random import randrange

def jokes(n):
    jokes_list = []
    for i in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))], adjectives[randrange(len(adjectives))]])
        jokes_list.append(joke)
    print(jokes_list)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

jokes(10)
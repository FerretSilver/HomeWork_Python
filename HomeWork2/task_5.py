#Реализуйте алгоритм перемешивания списка.
import random
n = int(input('Введите количество элументов списка: '))
ls = []
# for i in range(n):
#     ls.append(random.randrange(-n, n)) #random.randrange(start, stop, step) - возвращает случайно выбранное число из последовательности
# print(ls)
# random.shuffle(ls) #random.shuffle(sequence, [rand]) - перемешивает последовательность (изменяется сама последовательность).
# print(f'Перемешанный список: {ls}')


[ls.append(random.randrange(-n, n)) for i in range(n)]
print(ls)
random.shuffle(ls)
print(ls)

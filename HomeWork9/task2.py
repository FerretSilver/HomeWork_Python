#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
from functools import reduce
n = int(input('Введите количество элементов списка: '))
arr = []
#new_arr = []
# for i in range(n):
#     arr.append(randint(0, 100))
#     new_arr = arr[1::2]
# print(arr)
# print(sum(new_arr))

[arr.append(randint(0, 100)) for i in range(n)] #Заполнение списка случайными числами
new_arr = reduce(lambda x, y: x + y, arr[1::2]) #reduce принимает два аргумента, один накапливает значение, 
                                                #второй - это следующий элемент последовательности.
                                                #Сама функция возвращает единственное значение.
print(arr)
print(new_arr)

#  Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import randint
n = int(input('Введите количество элементов списка: '))
my_list = []
for i in range(n):
     my_list.append(randint(0, 100) / 10)
print(my_list)
print(max(my_list) - min(my_list))
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
n = int(input('Введите количество элементов списка: '))
arr = []
new_arr = []
for i in range(n):
    arr.append(randint(0, 10))
for i in range((len(arr)+1)//2):
    new_arr.append(arr[i]*arr[len(arr)-1-i])

print(arr)
print(new_arr)
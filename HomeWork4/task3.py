# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
my_list = [1, 1, 2, 3, 4, 5, 5]
unique_list = []

for i in my_list:
    count = 0
    for j in my_list:
        if i == j:
            count +=1
    if count == 1:
        unique_list.append(i)
print(f'Дан список: {my_list}\nНеповторяющиеся элементы списка: {unique_list}')
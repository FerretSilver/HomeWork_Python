# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]
n = int(input('Введите число: '))
multiplier = []
d = 2
m = n # Запомним исходное число
while d * d <= n:
        if n % d == 0:
            multiplier.append(d)
            n//=d
        else:
            d += 1
multiplier.append(n) # Добавим последнеё простое число
print(f'{m} = {multiplier}')
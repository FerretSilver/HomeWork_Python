# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11

number = float(input('Введите дробное число: '))

def sum_number(number):
    summ = 0
    for i in str(number):
        if i.isdigit():
            summ += int(i)
    return summ

print('Суммф цифр дробного числа равняется: ', sum_number(number))
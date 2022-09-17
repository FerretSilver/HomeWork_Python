# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

from math import pi
def toFixed(numObj, digits=0): # задает количество знаков после запятой( пример :) нашел на stackoverflow)
    return f"{numObj:.{digits}f}"

def count_number(number: float): # считает сколько знаков после запятой
    count = 0
    while number != 1:
        number *= 10
        count += 1
    return count
d = float(input('Задайте точность числа пи: '))
a = pi
print(f' Число Пи с заданной точноcтью {d} = {toFixed(a, count_number(d))}')


import math # Встроенный модуль math предоставляет набор функций для выполнения математических операций.
def digit_factorial(num):
    array = [1]
    for i in range(1, num):
        array.append(array[i-1] * (i+1)) # добавление последовательности произведений факториала
    return array
n = int(input("Введите число n (факториала): "))
print(f"Произведение чисел от 1 до {n} = {digit_factorial(n)} = {(math.factorial(n))}")
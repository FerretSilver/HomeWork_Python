#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def is_statement(x, y, z):
    print(f"Проверка истинности утверждения: ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) ==(not x and not  y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
is_statement(0, 0, 0)
is_statement(0, 0, 1)
is_statement(0, 1, 1)
is_statement(1, 1, 1)
is_statement(1, 0, 1)
is_statement(1, 1, 0)
is_statement(0, 1, 0)
is_statement(1, 0, 0)





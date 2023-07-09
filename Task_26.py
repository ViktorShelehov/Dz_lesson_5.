# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def power_recursive(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power_recursive(a, -b)
    elif b % 2 == 0:
        half = power_recursive(a, b // 2)
        return half * half
    else:
        return a * power_recursive(a, b - 1)

A = int(input('Введите число А: '))
B = int(input('Введите число B: '))
result = power_recursive(A, B)
print(result)  
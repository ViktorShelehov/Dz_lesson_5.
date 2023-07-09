# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def sum_recursive(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum_recursive(a - 1, b + 1)


num1 = int(input('Введите первое, целое неотрицательное число: '))
num2 = int(input('Введите второе, целое неотрицательное число: '))
result = sum_recursive(num1, num2)
print(result)  
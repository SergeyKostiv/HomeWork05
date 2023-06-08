# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def Chek(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return("Нет, Число не простое")
    
#         return("Да, Число простое")    
# number = int(input("Ввeдите число: "))
# res = Chek(number)
# print(res)   

# Rekursia
# def prime_number(n, i=2):
#     if n == 1 or n == 2:
#         return True
#     elif n % i == 0:
#         return False
#     elif i*i>n:
#         return True 
#     return prime_number(n, i+1)

# print(prime_number())


# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def pos(number):
    
#     if number == 0:
#         return " "
#     x = int(input("Введите число: "))
#     return pos(number-1)+str(x)
# number = int(input("Введите количество элементов: "))
# print(pos(number))

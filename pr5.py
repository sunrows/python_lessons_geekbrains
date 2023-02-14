# Задача 1 . Нужно вычислить число фибоначчи по индексу

# def fibonacci(num):
#     if num == 0:
#         fib = 0
#     elif num == 1:
#         fib = 1
#     else:
#         fib = fibonacci(num-1) + fibonacci(num-2)
#     return fib

# n = int(input())
# for i in range(n):
#     print(fibonacci(i))





# Задача 2.
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# n = int(input('Введите количество оценок: '))
# list_1 = []

# min_mark = 5
# max_mark = 0
# list_1 = [int(input(f'Введите оценку: ')) for i in range(n)]
# for i in list_1:
#     if i < min_mark:
#         min_mark = i
#     if i > max_mark:
#         max_mark = i
# print(min_mark, max_mark)
# print(list_1)

# for i in range(len(list_1)):
#     if list_1[i] == min_mark:
#         list_1[i] = max_mark
# print(list_1)

# от препода
# import random
# import time
# magazine = [random.randint(2, 5) for _ in range(10)]
# # list comprehension
# start = time.perf_counter()
# maxx = max(magazine)
# minn = min(magazine)
# end = time.perf_counter()
# print(magazine)

# for ind in range(0, len(magazine)):
#     if magazine[ind] == maxx:
#         magazine[ind] = minn
# print(magazine)



# Задача 3
# Напишите функцию, которая принимает одно число и проверяет, являетс          return "не простое"         return 'простое'



# def searchnumbers(n):
    
#     for i in range(2, n):
#         if(n%i == 0):
#             return ' не простое'
#         return 'простое'
# print (searchnumbers(12))

#от препода
# n = int(input()) # 20 -> 2, 4, 5, 10
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         print('Число не является простым')
#         break
# else:
#     print('Простое')
    


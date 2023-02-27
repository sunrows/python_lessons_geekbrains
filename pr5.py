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
    

#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# beries_list = [int(input('Введите кол-во ягод: ')) for _ in range(int(input('Введите кол-во кустов: ')))]
# # 3 2 5 7 1 4 8
# maxx = 0
# for ind in range(0, len(beries_list)):
#     if beries_list[ind] + beries_list[ind - 1] + beries_list[ind - 2] > maxx:
#         maxx = beries_list[ind] + beries_list[ind - 1] + beries_list[ind - 2]
#         print(maxx)


#Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.


# scrabble = {'AEIOULNSTRАВЕИНОРСТ':1,
# 'DGДКЛМПУ':2,
# 'BCMPБГЁЬЯ':3,
# 'FHVWYЙЫ':4,
# 'KЖЗХЦЧ':5,
# 'JZШЭЮ':8,
# 'QZФЩЪ':10}

# word = input().upper()
# points = 0
# for letter in word:
#     for el in scrabble:
#         if letter in el:
#             points += scrabble[el]
# print(points)



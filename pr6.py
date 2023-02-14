#Задача 39: Даны два массива чисел. Требуется вывести те элементы первого массива 
#(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
#Пользователь вводит число N - количество элементов в первом массиве,
#затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
#Затем элементы второго массива.
# array = [1,2,3,4]
# array_1 = [2,5,3,6]
# array_2 = []
# for i in array:
#     if array_1.count(i) < 1:
#         array_2.append(i)
# print(array_2)



# Решение преподавателя
# import random
# import time
# first_list = [random.randint(1, 100) for _ in range(10 ** 6)]
# second_list = [random.randint(1, 100) for _ in range(10 ** 6)]

# start = time.perf_counter() # для подсчета времени выполнения программы.


# for el in first_list:
#     if el not in second_list:
#         print(el)


# end = time.perf_counter()
# print(end - start)

# start = time.perf_counter()
# second_set = set(second_list)
# for el in first_list:
#     if el not in second_set:
#         print(el)
# end = time.perf_counter()
# print(end - start)
    



# 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество
# элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится
# число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


# array = [1,5,3,4,7,3,8,5]

# for i in range(1,(len(array)-1)):
#     if (array[i]>array[i-1] and array[i+1]<array[i]):
#         print(array[i])
#     else:
#         print(0)


# 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два
# элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# array = [1,5,3,4,7,3,6,4]

# for i in range(len(array)):
#     for j in range(i+1,len(array)):
#         if array[i] == array[j]:
#             print(f"{array[j]}, повторяется")

# Решение от преподавателя:

# some_list = []
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     some_list.append(number)
#
# count_dict = {}  # 2: 2, 3: 3, 4: 1, 5: 1
#
# for el in some_list:
#     if count_dict.get(el):
#         count_dict[el] += 1
#     else:
#         count_dict[el] = 1
#
# count = 0
# for value in count_dict.values():
#     count += value // 2
# print(count)

# some_dict = {1: 4, 4: 8}
# print(some_dict.get(5, 'Такого ключа нет!'))



# 45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному
# числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход 
# одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое
# из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара
# должна быть выведена только один раз (перестановка чисел новую пару не дает).


# def sum_div(n):
#     summa = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             summa += i
#     return summa


# summ_dict = {}  # 284: 220,

# k = int(input())
# for number in range(2, k + 1):
#     if number in summ_dict:
#         if sum_div(number) == summ_dict[number]:
#             print(number, summ_dict[number])
#     summ_dict[sum_div(number)] = number
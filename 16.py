# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#  В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример

# 5
# 1 2 3 4 5
# 3
# -> 1
n = int(input(' Введите кол-во элементов массива:'))
a = [0] * n  # Хитрый прием создать с нулевыми значениями список.
c = 0
print(len(a))
for i in range(n):
    a[i] = int(input())

b = int(input(' Введите разыскиваемое число:'))
for i in range(n):
    if b == a[i]:
        c += 1
print (c)




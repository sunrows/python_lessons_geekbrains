# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 6
# -> 5


x = int(input('Введите X: '))
# print ( list(range(1, int(input('Введите N: ')) + 1, 1) ) + [X])   - Можно вот так 
n = int(input('Введите N: '))
a = list(range(1,n+1,1))
a += [x]
print(a)


# Работа с файлами
# https://smartiqa.ru/python-workbook/file
#with open ('somefile.txt', 'modes', encoding = 'utf-8') as file 
#modes=>
# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись


# При работе с файлами в Python используется ряд функций и методов:
# - функция open() - открывает файл для чтения, записи, добавления нового содержимого. Может принимать дополнительные параметры: для задания режима открытия, 
# указания кодировки, вывода ошибок и др. Возвращает дескриптор файла, который обязательно нужно закрыть, 
# иначе файл останется в памяти. Дескриптор в данном случае представляет собой путь к документу в виде строки;
# - функция close() - закрывает файловый объект;
# - инструкция with (позволяет автоматически закрывать файловый объект после работы с ним);
# - метод read() - для чтения содержимого документа;
# - метод readlines() - преобразует все строки файла в список;
# - метод readline() - построчно выводит данные файла (удобно при работе с массивными документами);
# - метод write() - записывает новую информацию в файл;
# - функция rename() из модуля os - переименовывает документ и др.





# with open('pr8_text.txt', 'r',encoding='utf-8') as file:
#     # text = file.read().splitlines()
#     # print(text)
#     while True:
#         line = file.readline()
#         print(line.strip()) #strip - удаляет табуляцию и новую строку и все ненужные пустые символы
#         if not line:
#             break
# # Можно указать файл которого не существует:
# with open ('pr8_newFileFromCode.txt','w',encoding='utf-8') as file:
#     some_list = ['привет', 'пока','здравствуйте']
#     for word in some_list:
#         file.write(word +'\n')


#Задача посчитать количество букв в файле:

# Сравним 2 метода по быстроте:
import time

# with open('test20.txt', 'r', encoding='utf-8') as file:
# find_letter = input()
# count = 0
# start = time.time()
# for letter in file.read():
# if letter == find_letter:
# count += 1
# end = time.time()
# print(count)
# print(end - start)


# with open('test20.txt', 'r', encoding='utf-8') as file:
# find_letter = input()
# start = time.time()
# print(file.read().count(find_letter))
# end = time.time()
# print(end - start)

# Задача 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# from random import randint
# n = int(input('Введите кол-во элементов в списке: '))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('les8test.txt', 'w', encoding='utf-8') as file:
#     for _ in range(randint(1, n)):
#         file.write(str(randint(0, n - 1)) + '\n')

# with open('les8test.txt', 'r', encoding='utf-8') as file:
#     mult = 1
#     for ind in file.read().splitlines():
#         mult *= some_list[int(ind)]
# print(mult)



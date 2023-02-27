# Задача 1 
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл 
# file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
#  что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела



# n = int(input(' Введите положительное количество последних строк:'))

# # В случае проверки укажите абсолютный путь к файлу.
# n = -n
# with open ('d:/yandex_disk/YandexDisk/geekbrains/python/python_lessons_geekbrains/dz8.txt','r',encoding='utf-8') as file: 
#     lines = file.readlines()
#     while n < 0 :
#         print(lines[n])
#         n += 1




# Задача №2
# Документ dz8.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

with open ('d:/yandex_disk/YandexDisk/geekbrains/python/python_lessons_geekbrains/dz8.txt','r',encoding='utf-8') as file: 
    
    maxx = 0 
    for line in file:
        words = line.split(' ')
        words = [line.rstrip() for line in words]
        print(words)

        for ind in range(len(words)):
            if maxx < len(words[ind]):
                maxx = len(words[ind])
                word = words[ind]
                print(" Самое длинное слово: " + word)
                print(f' Количество символов: {maxx}')
            elif maxx == len(words[ind]):
                print("Еще нашлась такой же длины: " + words[ind])
    
    




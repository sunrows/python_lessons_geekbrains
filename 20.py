# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
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
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# пример

# Ввод:
# ноутбук
# Вывод:
# 12


### Scrubble game 

a = list(input().upper())

print(a)
pointOfScrubble = 0
for i in range(len(a)):
    if (a[i] == 'A' or a[i] == 'E' or a[i] == 'I' or a[i] == 'O' or a[i] == 'U' or a[i] == 'L' or a[i] == 'N' or a[i] == 'S' or a[i] == 'T' or a[i] == 'R' or\
        a[i] == 'А' or a[i] == 'В' or a[i] == 'Е' or a[i] == 'И' or a[i] == 'Н' or a[i] == 'О' or a[i] == 'Р' or a[i] == 'С' or a[i] == 'Т' ) :
        pointOfScrubble += 1
    elif(a[i] == 'D' or a[i] == 'G' or a[i] == 'Д' or a[i] == 'К' or a[i] == 'Л' or a[i] == 'М' or a[i] == 'П'  or a[i] == 'У') :
        pointOfScrubble += 2
    
    elif(a[i] == 'B' or a[i] == 'C' or a[i] == 'M' or a[i] == 'P' or a[i] == 'Б' or a[i] == 'Г' or a[i] == 'Ё'  or a[i] == 'Ь'  or a[i] == 'Я') :
        pointOfScrubble += 3
    elif(a[i] == 'F' or a[i] == 'H' or a[i] == 'V' or a[i] == 'W' or a[i] == 'Y' or a[i] == 'Й' or a[i] == 'Ы') :
        pointOfScrubble += 4
    elif(a[i] == 'K' or a[i] == 'Ж' or a[i] == 'З' or a[i] == 'Х' or a[i] == 'Ц' or a[i] == 'Ч') :
        pointOfScrubble += 5
    elif(a[i] == 'J' or a[i] == 'X' or a[i] == 'Ш' or a[i] == 'Э' or a[i] == 'Ю') :
        pointOfScrubble += 8
    elif(a[i] == 'Q' or a[i] == 'Z' or a[i] == 'Ф' or a[i] == 'Щ' or a[i] == 'Ъ') :
        pointOfScrubble += 10
    else:
        print(f' Возможно {a[i]} число или недопустимое значение!')
print(f'Point of your Scrubble = {pointOfScrubble}')        
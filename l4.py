# На лекции сегодня: 
#     Анономиные функции
#     фугкция map
#     функция filter
#     функция zip
#     функция enumerate
#     ФАйлы: Чтения и запись
#     Модуль OS
#     модуль Shutil

#-------------------------------------------------------------------
# def f(x):
#     return a+a
# a = f 
# print(type(a))  # Напишет: <class 'function'>
# print(a(5))  # Вычислит как будто функция f(x)
#-------------------------------------------------------------------

# Переименование функции
# Т.Е.  Если "f" - ссылается на ячейку памяти где записан код данной функции (f(x))
#       Значит можем вставить другую переменную которая также будет ссылаться на этот код 
#       (На функцию через указания просто имени Функции!!!) (Переименовали функцию)

def calk1(a):
    return a+a
def calk2(a):
    return a*a

# Функция math принимает 2 аргумента (op, x) => 
# внутри функции из двух аргументов делает функцию (op(x)), присваивает и выводит на экран.
def math(op,x):
    a = op(x) # Весь прикол кроется здесь!!!  Когда вызиваем функцию math(arg1, arg2)-
              # то внутри функции он из 2-ух ВХОДНЫХ аргументов создает функцию типа arg1(arg2)
    print(a)
math(calk1,5) # Функция math принимает 2 аргумента, первый аргумент ссылается на функцию (calk1) 
              #  далее функция принимает аргумент (a) и считает как нужно! 
              # буквально функция math создает внутри из двух аргументов функцию, и выполняет его и присвоет к переменной! 
              
# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# d g h t r g r h t j h b v f d s d f

# d g h t r g_2 r_2 h_2 t_2 j h_3 b v f d_2 s d_3 f_2

list = ['d', 'k', 'l', 'm', 'k', 'd', 'm', 'd']
count = {'d': 0, 'k': 0, 'l': 0, 'm': 0}
# s = list[0]
for i in range(len(list)):
    s = list[i]
    if s == list[i]:
        count[list[i]] += 1
print(count)

# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# (('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))
'''по условию вывод не требуется,но я для наглядности оставила'''
text = input('Введите строку house=дом car=машина men=человек tree=дерево: ')
print(text)
res_dict = dict((a.strip(), b.strip()) for a, b in (element.split('=') 
                                                    for element in text.split(' ')))
print(res_dict)
tp = tuple(map(lambda x: x, res_dict.items()))
print(tp)

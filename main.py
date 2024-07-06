# with open('my_file.txt', 'r') as file:
#     for string in file:
#         string = string.split(' ')
#         for i in string:
#             print(int(i)+1, end='')
#         print()


# Подсчитай количество единиц в файле.
# with open('my_file.txt', 'r') as file:
#     var = file.read()
#     var = var.replace('\n', ' ')
#     result = var.count('1')
# print(result)


# Найди и выведи на экран 8 элемент 14 строки.
# with open('my_file.txt', 'r') as file:
#     var = file.readlines()
#     result = []
#     for i in var:
#         i = i.replace('\n', '').split(' ')
#         result.append(i)
#     print(result[13][7])


# Найди сумму всех элементов в файле.
# with open('my_file.txt', 'r') as file:
#     var = file.read()
#     var = var.replace('\n', ' ').split(' ')
#     # print(var)
#     var = list(map(int, var))
#     result = sum(var)
# print(result)

# with open('my_file.txt', 'r') as file:
#     var = file.readlines()
#     result = []
#     for i in var:
#         i = i.replace('\n', '').split(' ')
#         result.append(list(map(int, i)))
# print(sum([sum(i) for i in result]))



# Найди и выведи на экран сумму элементов в 3, 6, 9 и 12 строках.
# with open('my_file.txt', 'r') as file:
#     var = file.readlines()
#     result = []
#     for i in var:
#         i = i.replace('\n', '').split(' ')
#         result.append(list(map(int, i)))
        
# print(sum(result[2]+result[5]+result[8]+result[11]))
        
        
# Найди сумму максимальных элементов во всех строках!

# Не знаешь, как найти максимум?

# Создай дополнительную переменную X для хранения максимума. Сравнивай каждый элемент строки с переменной X. 
# Если очередной элемент строки стал больше, чем значение переменной X — запиши этот элемент строки в переменную X.

with open('my_file.txt', 'r') as file:
    var = file.readlines()
    result = []
    for i in var:
        i = i.replace('\n', '').split(' ')
        result.append(max(list(map(int, i))))
        
print(sum(result))
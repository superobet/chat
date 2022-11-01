# Создайте список и введите его значения. Найдите наибольший и наименьший элемент списка,
# а также сумму и среднее арифметическое его значений.



# parametr = [1,4,5,6,11,2]
# minimum = min(parametr)
# maximum = max(parametr)
# vse = sum(parametr)
# kol = len(parametr)
# print(minimum)
# print(maximum)
# print(vse/kol)
#


# Задание 4
#
# Напишите рекурсивную функцию, которая вычисляет сумму натуральных чисел, которые входят в заданный промежуток.


# a = int(input("input digit a "))
# b = int(input("input digit b "))
# x = a
# sps = [a, b]
#
#
# def loop():
#     global x
#     if x != b-1:
#         x += 1
#         sps.append(x)
#         loop()
#     else:
#         print(sum(sps))
#
#
# loop()

# Задание 4
#
# Создайте список, введите количество его элементов и сами значения, выведите эти значения на экран в обратном порядке.


sps = []
x = int(input("how many in sps? "))
for i in range(x):
    j = input()
    sps.append(j)

print("- - - - - - - ")
new_sps = reversed(sps)
for j in new_sps:

    print(j)








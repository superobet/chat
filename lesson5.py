# def name():
#     name = input("my name? ")
#     if name == "":
#         print("Hello Evgen")
#     else:
#         print("Hello " + name)
#
#
# name()


#
# [-5,-3,0,1,2,4,43]      ---->   4  []
#                         ---->   1  [-3,4,0,1]
#                         ---->   6  [2,4]
#
# Задание 3
# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста.


# # text = input("Print your text " )
# text1 = ['а', 'и', 'к', 'о', 'с', 'с', 'с']
# # text2 = ", сосиска ".join(text1)
# text1 = input("enter something: ")
# j = 0
# text2 = ""
# for i in text1:
#     j+=1
#     if j % 2 ==0:
#         text2 += i.capitalize()
#     else:
#         text2 += i
#
# print(text2)
# # print(sorted(text))


text1 = "wqewqde"
text2 = "sdafd"
text1_1 = ""
for i in text1:
    for d in text2:
        if i == d:
            text1_1 += d
print(text1_1)







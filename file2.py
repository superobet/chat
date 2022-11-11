# file = open("text.txt", "r")
# x = 0
# for i in file.readlines():
#     x += int(i)
# print(x)
# file.close()


# импортирую библиотеку
import json

# загружаю файл
x = open("data.json")

# переконвертирую текст в формат json ( для того чтобы брать значения)
data = json.load(x)

print(data["name"])
x.close()

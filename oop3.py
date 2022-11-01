# class books:
#     def __init__(self, autor, name, year, theme):
#         self.autor = autor
#         self.name = name
#         self.year = year
#         self.theme = theme
#
#     def __str__(self):
#         return "Kniga avtora" + self.autor + "pid nazvoy" + self.name + str(self.year) + "roku " \
#                                                                                          "vipusku za temoy" + self.theme
#
#     def __repr__(self):
#         return "Repr starter Kniga avtora" + self.autor + "pid nazvoy" + self.name + str(self.year) + "roku " \
#                                                                                                       "vipusku za temoy" + self.theme
#
#     def __eq__(self, other):
#        if self.name==other.name:
#            return "This is the same book"
#        else:
#            return "This is not the same book"
#
# book1 = books("Shevchenko", "Zapovit", 1812, "death")
# book2 = books("Shevchenko", "Zapovit", 1812, "death")
# red = books("No name", "Images", 1990, "fun")
# dictionary = books("Slovar", "Letters", 992, "learning")
# print(repr(book1))
# print(book1 == book2)



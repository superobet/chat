# 1 question
"""
a = int(input("a = "))
b = int(input("b = "))
"""

n = int(input("n = "))


def factorial(n):
    i = 1
    for j in range(1, n):
        i *= j
    print(i)


factorial(n)

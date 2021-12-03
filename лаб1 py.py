import math

a = int(input("Введите А : "))
b = int(input("Введите И : "))

z = math.sin(a + b) * math.sin(a - b)
print(z)
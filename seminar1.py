#1. является ли одно число квадратом другого

# def square(a,b):
#     if a == b**2:
#         print(f"число {a} является квадратом {b}")
#     else:
#         print(f"число {a} не является квадратом {b}")

# square(5,5)

#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# def number(a,b,c,d,f):
#     max = 0
#     if (a > b) and (a > c) and (a > d) and (a > f):
#         max = a
#     elif (b > c) and (b > d) and (b > f):
#         max = b
#     elif (c > d) and (d > f):
#         max = c
#     elif (d > f):
#         max = d
#     else:
#         max = f
    
#     print(f"max = {max}")

# number(11,23,3,48,510)

#3 Вывести на экрна числа от минус n до n

# def num(n):
#     sum = ""
#     for i in range (-n, n + 1):
#         sum += f"{i} "
#     print (sum)

# num(5)

#4 Показать первую цифру дробной части числа
# def First_Number(number):
#     bof = int((number*10)%10)
#     print(bof)
# First_Number(489.199)

#5 Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# def num(n):
#     if (n % 5 == 0) and (n % 10 == 0) and (n % 15 == 0) and (n % 30 != 0):
#         print('true')
#     else:
#         print('false')

# num(30)

#6 Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# def day(n):
#     days = {1 : "monday", 2 : "tuesday", 3: "wednesday", 4: "thursday", 5 : "friday", 6 : "saturday", 7 : "sunday"}
#     if n in days:
#         print(days[n])

# day(5)

#7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

#8 Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 
#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
#Найти расстояние между двумя точками пространства

# def coordinates(x, y):
#     if (x > 0) and (y > 0):
#         print(f"Первая четверть")
#     elif (x > 0) and (y < 0):
#         print(f"Вторая четверть")
#     elif (x < 0) and (y > 0):
#         print(f"Четвертая четверть")
#     elif (x < 0) and (y < 0):
#         print(f"Третья четверть")
#     else:
#         print("точка лежит на оси")

# coordinates(10.3, 20.8)

def coor(a,b):
    print([['1', '2'], ['3', '4']][b < 0][a < 0])

coor(-4,-7)
# !!! Спаибо за комментарии к предыдущей домашней работе.
# Сейчас постаралась сделать все без вспомогательных методов.
# еще на семинаре услышала, что вам удобнее все читать в одном файле, поэтому решала все в одном

from calendar import month_name
import math
import random
from random import randint
import os
os.system('cls||clear')

# 1. Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

# arr = [1,2,3,4,5, 6] 
# sum_odd_elem = 0
# for element in arr:
#     if (element % 2 != 0):
#         sum_odd_elem += element

# print(sum_odd_elem)

# !!! я не поняла задание, 
# так как в нем было написано найти сумму чисел списка на нечетной позиции, 
# но в примере была сумма просто нечетных чисел
# поэтому я решила и так и так:

# sum_odd_index = 0
# for element in arr:
#     if (arr.index(element) % 2 != 0):
#         sum_odd_index += element

# print(sum_odd_index)


# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# arr = [2, 3, 4, 5, 6] #[2, 3, 5, 6]
# new_arr = []
# length = len(arr)
# for elem in arr:
#     if(length > len(arr)/2):
#         new_arr.append(elem * arr[length - 1])
#         length -= 1

# print(new_arr)


# 3. В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# array = [1.1, 1.2, 3.1, 5, 10.01]
# new_arr = []

# for element in array:
#     new_arr.append((element - round(element)))

# print(new_arr)

# max = new_arr[0]
# min = new_arr[0]
# for elem in new_arr:
#     if(round(elem, 2)) > max:
#         max = round(elem, 4)
#     if(round(elem, 2)) < min:
#         min = round(elem, 4)

# print(max - min)   #!!! у меня получилось в ответе 0,2 а не 0,19 так как самое маленько дробное число это ноль - от пятерки.


# Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.

# array = [randint(0,1) for i in range(6)]
# print(f"Число в двоичной системе  -  {array}")
# len = len(array) - 1
# sum = 0

# for elem in array:
#     sum += (2**len)*elem
#     len -= 1

# print(f"Число в десятичной системе - {sum}")

# 2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. 
# Игра работает так: Случайным образом генерируйте 4-значное число. 
# Попросите пользователя угадать 4-значное число. 
# За каждую цифру, которую пользователь правильно угадал в нужном месте, 
# у них есть “корова”. За каждую цифру, которую пользователь угадал правильно, 
# в неправильном месте стоит “бык”. Каждый раз, когда пользователь делает предположение, 
# скажите им, сколько у них “коров” и “быков”. 
# Как только пользователь угадает правильное число, игра окончена. 
# Следите за количеством догадок, которые пользователь делает на протяжении всей игры, 
# и сообщите пользователю в конце.

# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, 
# которые не превышают четыре миллиона.

# 4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

# 5.2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?
# 2
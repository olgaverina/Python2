# !!! Спаибо за комментарии к предыдущей домашней работе.
# Сейчас постаралась сделать все без вспомогательных методов.
# еще на семинаре услышала, что вам удобнее все читать в одном файле, поэтому решала все в одном

from calendar import month_name
import math
import random
from random import randint
import os
os.system('cls||clear')

print("1. Найти сумму чисел списка стоящих на нечетной позиции")
# Пример:[1,2,3,4] -> 4

arr_list = [1,2,3,4,5, 6] 
sum_odd_elem = 0
for element in arr_list:
    if (element % 2 != 0):
        sum_odd_elem += element

print(f"\nСумма нечетных чисел - {sum_odd_elem}\n")

# !!! я не поняла задание, 
# так как в нем было написано найти сумму чисел списка на нечетной позиции, 
# но в примере была сумма просто нечетных чисел
# поэтому я решила и так и так:

sum_odd_index = 0
for element in arr_list:
    if (arr_list.index(element) % 2 != 0):
        sum_odd_index += element

print(f"Сумма чисел на нечетных индексах - {sum_odd_index}\n")


print("2. Найти произведение пар чисел в списке. \
\nПарой считаем первый и последний элемент, второй и предпоследний и т.д.\n") 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

ar = [2, 3, 4, 5, 6] #[2, 3, 5, 6]
new_ar = []
length = len(ar)
for elem in ar:
    if(length > len(ar)/2):
        new_ar.append(elem * ar[length - 1])
        length -= 1
print(f"Список - {ar}")
print(f"\nПроизведение пар чисел этого списка - {new_ar}\n")


print("3. В заданном списке вещественных чисел найдите разницу \
\nмежду максимальным и минимальным значением дробной части элементов.")
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.134, 1.234, 3.134, 5, 10.01]
new_arr = []

for element in list:
    new_arr.append((element - round(element)))

print(f"\nМассив с дробными частями чисел - {new_arr}\n")

max = new_arr[0]
min = new_arr[0]
for elem in new_arr:
    if(round(elem, 2)) > max:
        max = round(elem, 4)
    if(round(elem, 2)) < min:
        min = round(elem, 4)

print(f"Разница между максимальным и минимальным значением дробной части - {max - min}\n")   #!!! у меня получилось в ответе 0,2 а не 0,19 так как самое маленько дробное число это ноль - от пятерки.


print("Экстра-задачи:\n")

print("1. Написать программу преобразования двоичного числа в десятичное.\n")

d_array = [randint(0,1) for i in range(6)]
print(f"Число в двоичной системе  -  {d_array}\n")
n_len = len(d_array) - 1
sum = 0

for elem in d_array:
    sum += (2**n_len)*elem
    n_len -= 1

print(f"Число в десятичной системе - {sum}\n")



# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. 
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, 
# которые не превышают четыре миллиона.

print(f"3. Найдите сумму всех четных элементов ряда Фибоначчи, \
которые не превышают четыре миллиона.")
print()
fib_arr = []
sum_even = 0
fib_arr.append(1)
fib_arr.append(2)

for i in range(1, 31):
    length = len(fib_arr)
    fib_arr.append(fib_arr[length - 2] + fib_arr[length - 1])
print(f"ряд Фибоначчи - {fib_arr}")

for i in range(0, len(fib_arr), 2):
    sum_even += fib_arr[i]

print(f"\nСумма - {sum_even}")


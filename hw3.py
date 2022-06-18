from operator import le
import random 
import os
import math
os.system('cls||clear')

print("1. Найти НОК двух чисел")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

max = a if a >= b else b #найти максимальное число
nod = 0                  #НОД
for i in range(1, max):
    if ((a % i == 0) and (b % i == 0) ):
        nod = i
nok = int(a * b / nod)
print(f"Наименьшее общее кратное чисел {a} и {b} - {nok}\n\n")


print("2. Вычислить число Пи c заданной точностью d\n") 
# Пример: при d = 0.001,  c= 3.141. 

# !!! Простите, я вообще не поняла эту задачу :(

pi = str(math.radians(180))
d = input("Введите число d в формате '0.001' : \n")

str = d.split(".")                      #отделила дробную часть
length = len(str[1])   
print(length)                 #посчитала ее длину
print(f"Настоящее число Пи - {pi}\n")                               
pi_short = pi.split(".")                #разделила пи на целую часть и дробную
result = pi_short[0] + "."              #вернула настоящее пи и точку
j = 0                  
for i in pi_short[1]:                   #добавляю обратно знаки после запятой - сколько нужно
    if (j < length): 
        result += i
    else:
        break
    j += 1

print(f"Число Пи с {length} знаками после запятой - {result}\n")

# print("\n3. Составить список простых множителей натурального числа N\n")
# n = int(input("Введите число: "))




# + на тему файловой системы:
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 



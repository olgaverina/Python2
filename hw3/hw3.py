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

# !!! Простите, я вообще не поняла эту задачу :( 001 - это 3 знака после запятой?

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

print("\n3. Составить список простых множителей натурального числа N\n")
num = int(input("Введите число: "))
simple_numbers = []

all_numbers = list(range(2, num + 1))      #выбросила единицу
for number in all_numbers:
    if number != 0:                         #проверяю были ли уже замены
        for n in range(2 * number, num+1, number):       
            all_numbers[n-2] = 0            #так как начала range с двойки
print(all_numbers)


for digit in all_numbers:
    if digit != 0:
        simple_numbers.append(digit)          #новый массив с не-нулями

print(simple_numbers)



print("4. Дана последовательность чисел.\n\
    Получить список неповторяющихся элементов исходной последовательности\n\
    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]\n")


array = [1, 2, 4, 7, 3, 5, 1, 5, 3, 10]
new_array = []

print(f"Список - {array}\n")
for i in array:
    if i not in new_array:
        new_array.append(i)

print(f"Новый список - {new_array}\n")

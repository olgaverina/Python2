print("1. Создать и заполнить файл случайными целыми значениями.\n\
Выполнить сортировку содержимого файла по возрастанию.")

import random

array = []

with open('file.txt', 'w+') as data:                        #записали в файл
    for i in range(1, 10):
        data.write(str(random.randint(0, 100)) + "\n")

with open('file.txt', 'r') as data:                         
    for d in data:
        array.append(int(d))                                #перезаписали в список, чтобы его отсортировать

print(f"Неотсортированный список: {array}")

def sort_array(arr):                                        #отсортировали список
    temp = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp  


sort_array(array)
print(f" Отсортированный список : {array}")

with open('file.txt', 'w+') as data:                      
    for i in array:
        data.write(str(i) + "\n")
# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
# сделать запись в файл


# import random 
# import os
# os.system('cls||clear')

# num = int(input("Enter the number: "))

# array = []
# rand_array = []

# def fill_array(arr, n): #Задать список из N элементов, заполненных числами из [-N, N]
#     for i in range(n):
#         arr.append(random.randint(-n, n))
#     return arr

# array = fill_array(array, num)
# print(array)

# def create_custom_arr(n): #Задать позиции элементов, которые генерятся рандомно
#     rand_arr = []
#     for i in range(0, n):
#         rand_arr.append(str(random.randint(0, n-1)))
#     return rand_arr

# element_positions = create_custom_arr(num)
# print(f'Elements positions: {element_positions}')

# def create_file(elements, n):
#     data = open('file.txt', 'w') #a - данные дозаписались
#     for e in elements:
#         data.writelines(f'{str(e)}\n')
#         #print(f'element - {e}')
#     data.close()

# create_file(element_positions, num)

# print()

# def read_file(arr):
#     prod = 1
#     data = open('file.txt', 'r')
#     for i in data:
#         print(i)
#         prod *= arr[int(i)]
#         print(arr[int(i)])
#     data.close()
#     return prod

# print(f'result = {read_file(array)}')




# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = int(input("Enter the number: "))

if n < 0:
    print("Wrong number")
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print(fib)

neg_fib = []

for i in range(1, n*2):
    if(i < n):
        if(i%2==0):
            neg_fib.append(fib[n-i]*-1)
        else:
            neg_fib.append(fib[n-i])
    else:
        neg_fib.append(fib[i-n])

print(neg_fib)



# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел 
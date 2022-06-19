print("5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.\n") 

def read_file():
    file_numbers = [0, 3, 5, 7, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #числовой массив
    print(f"Исходный массив - {file_numbers}\n")
    data = open('numbers.txt', 'w+')
    odd_arr = []                                 
    for lin in file_numbers:
        data.write(str(lin) + "\n")           #записываем массив в файл
        if((int(lin)) % 2 != 0):              ##находим в нем нечетные числа, переносим их в другой массив
            odd_arr.append(int(lin))
    data.close()
    print(f"Нечетный массив - {odd_arr}\n")
    data = open('numbers.txt', 'w+')        #перезаписываем исходный массив нечетными числами из нового массива
    for l in odd_arr:
        data.write(str(l) + "\n")
    data.close()

read_file()
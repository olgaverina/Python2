# 2. Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие максимальное 
# количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

array = [1, 5, 2, 3, 4, 6, 1, 7, 10]


max_arr = []
max_len_array = 0

for i in range(0, len(array)):
    current_arr = []
    current_arr.append(array[i])
    current_len_arr = 1               #
    max = array[i]
    for j in range(1, len(array)):
        if (((i + j < len(array)) and array[i + j] > max)):
            current_arr.append(array[i + j])
            max = array[i + j]
            current_len_arr += 1
    if (max_len_array < current_len_arr):
        max_len_array = current_len_arr
        max_arr = current_arr


print(f"Max array - {max_arr}")


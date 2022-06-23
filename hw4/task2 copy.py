# 2. Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие максимальное 
# количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя


array = [1, 5, 2, 3, 4, 6, 1, 7]    # => [1, 2, 3, 4, 6, 7]
array2 = [5, 2, 3, 4, 6, 1, 7]      # => [2, 3, 4, 6, 7]
array3 = [1, 8, 6, 5, 2, 8, 3, 8, 4, 6, 1, 7, 8, 9, 10]

print(array)

def find_max(array):
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

    return (max_arr)

# def maximum(arr):
#     max = arr[0]
#     for i in range(1, len(arr)):
#         if (max < arr[i]):
#             max = arr[i]
#     return max

total_new_arr = []
for i in range(0, len(array)):
    total_new_arr.append(find_max(array[i]))

print(total_new_arr)
print(f"Max array1 - {find_max(array)}")

#print(f"Max array2 - {find_max(array2)}")

#print(f"Max array2 - {find_max(array3)}")

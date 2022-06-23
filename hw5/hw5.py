# 1. Напишите программу, удаляющую из текста все слова содержащие "абв",
# которое регистронезависимо. Используйте знания с последней лекции. 
# Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

text = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
substr = "абв"
splitted_arr = text.split()
print(splitted_arr)

def delete_line(long_line, short_line):
    new_arr = []
    for s in long_line:
        s = s.lower()
        if short_line not in s:
            new_arr.append(s)
    return(new_arr)

print(delete_line(splitted_arr, substr))


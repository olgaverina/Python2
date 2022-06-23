# Экстра-задачи:
# 1. Давайте представим, что ваша компания только что наняла вашего друга из колледжа и 
# заплатила вам реферальный бонус. Потрясающе! Чтобы отпраздновать, вы берете свою команду 
# в очень странный бар по соседству и используете реферальный бонус, чтобы купить и построить 
# самую большую трехмерную пирамиду из пивных банок, которую вы можете.
# Пирамида пивных банок будет квадратировать количество банок на каждом уровне - 1 банка на верхнем уровне, 
# 4 на втором, 9 на следующем, 16, 25...
# Определите функцию beeramid, чтобы вернуть количество полных уровней пирамиды пивных банок, 
# которую вы можете сделать, учитывая параметры: реферальный бонус и цена пивной банки.
# Например:
# beeramid(1500, 2)# 12
# beeramid(5000, 3)# 16

import math

bonus = 1500
price = 2

def beeramid(b, p):
    count = 0
    bottles_amount = b//p
    while(b):
        bottles_amount = math.sqrt(bottles_amount)
        count += 1
        b = b - bottles_amount*price
    return(count)

print(beeramid(bonus, price))



# 2. Создать функцию, которая из списка чисел возвращает число, 
# являющее суммой двух или нескольких других элементов, либо возвращающее None, если такого числа нет.

# 3. Вот вам файл с английскими именами. https://cloud.mail.ru/public/J7aq/iHnLspVJR
# Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и 
# умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.

# Например, если список отсортирован по алфавиту, имя COLIN 
# (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке. 
# Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

# Какова сумма очков имен в файле?


# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def count_int(nums, num):
    return str(nums).count(str(num))


nums = 32545223
num = 5
print(count_int(nums, num))
nums = 415456
num = 1
print(count_int(nums, num))

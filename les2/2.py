#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def Count_even_and_odd(nums):
    even = 0
    odd = 0
    for i in str(nums):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1

    return (f"В числе {nums}, {even} - четных и {odd} - нечетных чисел")


num = 34560
print(Count_even_and_odd(num))
num = 112
print(Count_even_and_odd(num))

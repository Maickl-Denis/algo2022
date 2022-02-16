#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
#   Количество элементов (n) вводится с клавиатуры.


def sum_elements(n):
    begin = 1
    sum = 0
    for i in range(n):
        sum += begin
        begin /= -2
    print(sum)

num = 2
sum_elements(num)
num = 4
sum_elements(num)
#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
def sum_ch(ch: int):
    sm = 0
    while ch > 0:
        sm = sm + ch % 10
        ch = ch // 10
    return sm

print(sum_ch(int(input())))

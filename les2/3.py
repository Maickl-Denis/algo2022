#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
#   введено число 3486, то надо вывести число 6843. (Сделать без использования строк)


def num_reverse(nums):
    while nums > 0:
        print(nums % 10, sep='', end='')
        nums = nums // 10


num = 34560
num_reverse(num)
#num = 112
#num_reverse(num)
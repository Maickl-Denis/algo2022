# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def max_sum_ch(nums):
    max_sum = 0
    for i in nums:
        next_sum = 0
        while int(i) > 0:
            next_sum += i % 10
            i = i // 10
        if max_sum < next_sum:
            max_sum = next_sum
    return max_sum




nums = [1, 5, 16, 9, 3, 254, 211]
print(max_sum_ch(nums))

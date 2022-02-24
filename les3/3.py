# 3. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

def min_ch(nums: list):
    min_n = 0

    for i in nums:
        if i < min_n:
            min_n = i
    if min_n == 0:
        return 'в массиве нет отрицательных чисел'
    else:
        return min_n

print(min_ch([1, 2, 3, 4]))
print(min_ch([1, -4]))
print(min_ch([2, -1, -5, 4]))

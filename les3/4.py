#4. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

def two_min(nums: list):
    min_one = 9999999
    min_two = 9999999

    for num in nums:
        if num < min_one:
            min_two = min_one
            min_one = num
        elif num < min_two:
            min_two = num
    return min_one, min_two

print(two_min([1, 2, 3, 4, 5]))
print(two_min([1, -4]))
print(two_min([2, -1, -5, 4]))

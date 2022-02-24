# 2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def min_max(nums: list):
    min_i = 0
    max_i = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[max_i]:
            max_i = i
        if nums[i] < nums[min_i]:
            min_i = i

    nums[min_i], nums[max_i] = nums[max_i], nums[min_i]

    return nums

print(min_max([1, 2, 3, 4]))
print(min_max([1, 4]))
print(min_max([2, 1, 5, 4]))

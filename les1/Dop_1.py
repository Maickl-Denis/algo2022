def removeDuplicates(nums):
    last = nums[0]
    j = 1

    for i in range(1, len(nums)):
        if nums[i] != last:
            nums[j] = nums[i]
            last = nums[i]
            j += 1
    for i in range(j, len(nums)):
        nums[i] = '_'
    return nums


ls = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(*removeDuplicates(ls))
ls = [1, 1, 2]
print(*removeDuplicates(ls))
ls = [1]
print(*removeDuplicates(ls))

def moveZeroes(nums):
    idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[idx] = nums[i]
            idx += 1
    for i in range(idx, len(nums)):
        nums[i] = 0
    return nums


ls = [0, 1, 0, 3, 12]
print(*moveZeroes(ls))
ls = [0]
print(*moveZeroes(ls))

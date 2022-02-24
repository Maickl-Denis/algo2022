class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set(i for i in nums)
        if len(nums) == len(st):
            return False
        else: return True
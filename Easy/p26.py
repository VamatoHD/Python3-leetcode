class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        x = 0
        for i in range(1, len(nums)):
            if nums[x] != nums[i]:
                x += 1
                nums[x] = nums[i]
        return x+1

#Bubble sort implementation
class Solution:
    def sortColors(self, nums) -> None:
         """
         Do not return anything, modify nums in-place instead.
         """
         l = len(nums)
         for i in range(l):
            for j in range(l-1):
               if nums[j]>nums[j+1]:
                  nums[j],nums[j+1] = nums[j+1],nums[j]

#Python sort implementation
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

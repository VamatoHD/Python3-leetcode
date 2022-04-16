#Solution 1 (slow)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        while 0 in nums:
            zeros +=1
            nums.remove(0)
        nums[:] = nums + [0]*zeros      
        
#Solution 2 (still slow)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        if count > 0:
            for i in range(count):
                nums.remove(0)
                nums.append(0)


#Solution 1
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        while low<=high:
            mid = (low+high)//2
            if not isBadVersion(mid-1):
                if isBadVersion(mid):
                    return mid
                else:
                    low = mid+1
            else:
                high = mid-1

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fl = nums1+nums2
        fl.sort()
        l = len(fl)
        return (fl[l//2-1]+fl[l//2])/2 if (l%2)==0 else fl[int(l/2)]
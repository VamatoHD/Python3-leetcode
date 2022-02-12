#Solution 1
class Solution:
    def romanToInt(self, s: str) -> int:
        map_ = {"I":1 ,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        i = len(s)-1
        val = 0
        while i>=0:
            if map_[s[i]] > map_[s[i-1]] and i!=0:
                val +=(map_[s[i]]-map_[s[i-1]])
                i-=1
            else:
                val +=map_[s[i]]
            i-=1
        return val

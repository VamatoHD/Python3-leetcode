#Solution 1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1
        else:
            return haystack.index(needle)

#Solution 2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1
            

#Solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if str(x)[::-1] != str(x) else True
    
#Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s==s[::-1]

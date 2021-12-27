class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if str(x)[::-1] != str(x) else True

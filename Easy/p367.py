class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = num**.5
        return True if n == int(n) else False

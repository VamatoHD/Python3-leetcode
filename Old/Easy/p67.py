#1 line function
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{:b}'.format(int(a,2)+int(b,2))

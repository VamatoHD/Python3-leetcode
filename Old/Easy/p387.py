class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = [s.index(I) for I in "abcdefghijklmnopqrstuvwxyz" if s.count(I) == 1]
        return min(i) if len(i) != 0 else -1

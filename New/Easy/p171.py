class Solution:
   def titleToNumber(self, columnTitle: str) -> int:
      n = columnTitle[::-1]
      return sum([
         (ord(n[i]) - 64) * (26**i)
         for i in range(len(columnTitle))
      ])
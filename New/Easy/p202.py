class Solution:
   def isHappy(self, n: int) -> bool:
      temp = set()
      while True:
         n = sum([int(i)**2 for i in str(n)])

         if n == 1:
               return True
         if n in temp:
               break

         temp.add(n)
      return False
                
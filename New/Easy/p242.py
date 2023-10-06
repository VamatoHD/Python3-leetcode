class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
      dic = {}
      for c in s:
         if not c in dic:
            dic[c] = 1
         else:
            dic[c] += 1

      for c in t:
         if not c in dic:
            return False
         else:
            dic[c] -= 1
      
      return all(v==0 for v in dic.values())
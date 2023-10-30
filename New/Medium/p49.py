class Solution:
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = {}

      for word in strs:
         a = "".join(sorted(word))
         if not a in res:
               res[a] = [word]
         else:
               res[a].append(word)

      return [x for x in res.values()]
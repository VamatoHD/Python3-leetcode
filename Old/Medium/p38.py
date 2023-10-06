class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        x = self.countAndSay(n-1)

        res = ""
        count = 1
        cur = x[0]

        for i in range(1,len(x)):
            if x[i] == cur:
                count += 1
            else:
                res += str(count) + str(cur)
                count = 1
                cur = x[i]
        res += str(count) + str(cur)
        return res
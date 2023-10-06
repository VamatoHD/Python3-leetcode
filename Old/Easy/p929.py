class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        a = []
        for x in emails:
            n = x.find("@")
            x = x[0:n].replace(".", "")+x[n:]
            if "+" in x:
                n = x.find("+")
                n1 = x.find("@")
                x = x.replace(x[n:n1], "")
            if not x in a:
                a.append(x)

        return len(a)

#Not the best but maybe I'll update it later
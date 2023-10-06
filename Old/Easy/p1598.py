class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = 0
        for i in logs:
            if i == "../" and s != 0:
                s -= 1
            elif not "." in i:
                s += 1
        return s

#It's one of my favorite problems.

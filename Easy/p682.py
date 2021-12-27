class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i == "D":
                a = int(stack.pop())
                stack.extend([a, 2*a])
            elif i == "C":
                stack.pop()
            elif i == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.extend([b, a, a+b])
            else:
                stack.append(int(i))

        return sum(stack)

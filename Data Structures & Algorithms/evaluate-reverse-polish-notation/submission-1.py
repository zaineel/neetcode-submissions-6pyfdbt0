class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        stack = []
        total = 0
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                else:
                    res = int(a / b)

                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]
        
class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            if stack and ch in hashMap:
                if stack[-1] == hashMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
class Solution:
    def isHappy(self, n: int) -> bool:
        cur = str(n)
        seen = set()
        while cur not in seen:
            ans = 0
            seen.add(cur)
            for num in cur:
                ans += int(num) ** 2
            if ans == 1:
                return True
            cur = str(ans)
        return False
        
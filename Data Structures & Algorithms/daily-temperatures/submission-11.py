class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
            curr = temperatures[i]
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= curr:
                j += 1
            if j < len(temperatures) and temperatures[j] > curr:
                res.append(j-i)
            else:
                res.append(0)
        res.append(0)
        return res

            
        
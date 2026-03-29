class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_list = sorted(nums)
        res = []
        for i in range(len(new_list) - 2):
            if i > 0 and (new_list[i] == new_list[i-1]):
                continue
            l, r = i+1, (len(new_list) - 1)
            while l < r:
                if new_list[i] + new_list[l] + new_list[r] == 0:
                    res.append([new_list[i], new_list[l], new_list[r]])
                    l += 1
                    r -= 1
                    while l < r and (new_list[l] == new_list[l-1]):
                        l += 1
                    while l < r and (new_list[r] == new_list[r+1]):
                        r -= 1
                    
                elif new_list[i] + new_list[l] + new_list[r] > 0:
                    r -= 1
                elif new_list[i] + new_list[l] + new_list[r] < 0:
                    l += 1
        return res
        
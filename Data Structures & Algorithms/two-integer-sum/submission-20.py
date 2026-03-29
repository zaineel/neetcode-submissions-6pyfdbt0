class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for i in range(len(nums)):
            hp[nums[i]] = i

        for i in range(len(nums)):
            res = target - nums[i]
            
            if res in hp:
                if hp[res] != i:
                    
                    return [i, hp[res]]

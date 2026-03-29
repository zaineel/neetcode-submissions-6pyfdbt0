class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        if len(nums) == 0:
            return False
        for i in range(len(nums)):
            if nums[i] in h:
                return True
            else:
                h[nums[i]] = h.get(nums[i], i)
        return False
        
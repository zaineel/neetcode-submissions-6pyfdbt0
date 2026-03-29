class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         # [ 1, 2, 3, 4, 5] lets say product at index 2 is?
         # it will product of 0th and 1st index * 3rd and 4th index
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1 , -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
        
        
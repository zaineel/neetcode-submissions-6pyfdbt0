class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        sorted_pairs = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)
        res = []
        for num, freq in sorted_pairs:
            if len(res) < k:
                res.append(num)
            else:
                break

        return res

        
            

        
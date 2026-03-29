class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        my_set = set()
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[i])
            length = max(length, i - l + 1)
        return length
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        max_freq = 0
        max_length = 0
        left = 0
        for right in range(len(s)):
            current_char = s[right]
            hmap[current_char] = hmap.get(current_char, 0) + 1
            max_freq = max(max_freq, hmap[current_char])
            replacements_needed = (right - left + 1) - max_freq
            while replacements_needed > k:
                char_to_remove = s[left]
                hmap[char_to_remove] = hmap.get(char_to_remove, 0) - 1
                left += 1
                replacements_needed = (right - left + 1) - max_freq
            max_length = max(max_length, right-left+1)
        return max_length


        
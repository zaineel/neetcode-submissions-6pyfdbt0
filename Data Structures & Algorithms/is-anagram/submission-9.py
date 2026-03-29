class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
        for i in range(len(t)):
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        for char in t_map:
            if t_map[char] != s_map.get(char, 0):
                return False
        return True

        
        
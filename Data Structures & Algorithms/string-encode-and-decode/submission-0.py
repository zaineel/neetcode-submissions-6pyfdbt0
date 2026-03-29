class Solution:

    def encode(self, strs: List[str]) -> str:
        builder = []
        for word in strs:
            length = len(word)
            builder.append(str(length) + "#" + word)
        return "".join(builder)        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            if s[j] == '#':
                length = int(s[i:j])
                j += 1
                word = s[j:j+length]
                res.append(word)
                i = j+length
                j = i
            else:
                j += 1
        return res


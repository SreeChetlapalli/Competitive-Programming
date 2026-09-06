class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        x = {}

        for i in s:
            if i in x.keys():
                continue
            else:
                x[i] = s.count(i)
        while len(s) - max(x.values()) > k:
            s = s[1:]
        return len(s) 
        
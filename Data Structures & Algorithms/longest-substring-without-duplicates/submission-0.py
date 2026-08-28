class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        x = 0
        y = {}
        k = 0

        for idx, i in enumerate(s):
            if i in y and y[i] >= k:
                k = y[i] + 1

            y[i] = idx

            if idx - k + 1 > x:
                x = idx - k + 1

        return x
        

                
        
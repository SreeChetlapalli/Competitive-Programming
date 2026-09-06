class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        y, x = [], []
        y.extend(s1)
        y.sort()
        x.extend(s2)
        x.sort()
        if s1 in s2:
            return True
        else:
            return False
        
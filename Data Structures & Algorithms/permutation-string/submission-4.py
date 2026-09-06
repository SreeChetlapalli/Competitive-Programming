class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = len(s1)
        y = []
        p = []
        y.extend(s1)
        y.sort()
        for i in range(len(s2) - x):
            k = s2[i:i+x]
            p.extend(k)
            p.sort()
            if p == y:
                return True
            p = []
        return False

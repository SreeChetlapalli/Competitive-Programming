class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x = {}
        y ={}
        for i in range(len(s)):
            if s[i] not in x:
                x[s[i]] = 1
            else:
                x[s[i]] +=1
            if t[i] not in y:
                y[t[i]] = 1
            else:
                y[t[i]] +=1
        for i in x:
            if x.get(i) != y.get(i):
                return False
        return True

            

        
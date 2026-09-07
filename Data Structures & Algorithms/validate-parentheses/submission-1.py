class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        for i in range(len(s)):

            if s[i] == "(":
                x.append(s[i])
            elif s[i] == "{":
                x.append(s[i])
            elif s[i] == "[":
                x.append(s[i])
            else:

                j = x.pop()
                if ord(j) - ord(s[i]) != 1 and ord(j) - ord(s[i]) != -1:
                    return True
        return False

            



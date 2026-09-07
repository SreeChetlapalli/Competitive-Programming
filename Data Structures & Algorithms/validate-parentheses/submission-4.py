class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        if len(s) % 2 !=0:
            return False

        for i in range(len(s)):

            if s[i] == "(":
                x.append(s[i])
            elif s[i] == "{":
                x.append(s[i])
            elif s[i] == "[":
                x.append(s[i])
            else:

                if len(x) == 0:
                    return False
                j = x.pop()
                if j == "{" and s[i] != "}" or j == "(" and s[i] != ")" or j == "[" and s[i] != "]":
                    return False
        if len(x) != 0:
            return False
        return True

            



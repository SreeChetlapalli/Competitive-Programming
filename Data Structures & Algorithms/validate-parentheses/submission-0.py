class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        x.extend(s)
        if len(x) % 2 != 0:
            return False
        y = -1
        i = 0  

        while s[i] == "[" or s[i] == "{" or s[i] == "(":
           
            if s[i] == "[" and s[y] != "]":
                return False    
           
            if s[i] == "(" and s[y] != ")":
                return False    
           
            if s[i] == "{" and s[y] != "}":
                return False    
            
            i +=1
            y -=1
        return True

            


        
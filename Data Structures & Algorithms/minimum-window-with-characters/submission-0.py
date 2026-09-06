class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        if t == s:
            return t
        dict1 = {chr(i): 0 for i in range(ord('A'), ord('z') + 1)}
        dict2 = {chr(i): 0 for i in range(ord('A'), ord('z') + 1)}  
        
        for i in t:
            if i in dict1.keys():
                dict1[i] +=1
            else:
                dict1[i] = 1

        x = 0
        y = 0
        min = ""
        while y < len(s):

            dict2[s[y]] += 1

            valid = True
            for key in dict1:
                if dict2[key] < dict1[key]:
                    valid = False
                    break

            while valid:
                if min == "" or y - x + 1 < len(min):
                    min = s[x:y+1]

                dict2[s[x]] -= 1
                x += 1

                valid = True
                for key in dict1:
                    if dict2[key] < dict1[key]:
                        valid = False
                        break

            y += 1
        return min
            

        
        







        
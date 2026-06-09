class Solution:
    def isPalindrome(self, s: str) -> bool:

        x=""
        for i in s:
            if i.isalnum():
                x+=i.lower()
        
        for i in range(len(x)//2):
            if x[i] != x[-1-i]:
                
                return False
        return True
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        x = ""
        y = ""
        for i in strs:
            x = i
            y = y + str(";") + i
        
        return y

    def decode(self, s: str) -> List[str]:
        x = list(s.split(";"))
        return x[1:]


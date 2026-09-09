class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        x = []
        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "/" or tokens[i] == "*" or tokens[i] == "-":
                y = x.pop()
                z = x.pop()
                if tokens[i] == "+":
                    x.append(y+z)
                elif tokens[i] == "-":
                    x.append(z-y)
                elif tokens[i] == "*":
                    x.append(y*z)
                elif tokens[i] == "/":
                    x.append(int(z / y))
            else:
                x.append(int(tokens[i]))
        return x[0]



        
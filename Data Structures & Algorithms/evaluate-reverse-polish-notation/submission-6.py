class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        x = []
        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "/" or tokens[i] == "*" or tokens[i] == "-":
                y = x.pop()
                z = x.pop()
                if tokens[i] == "+":
                    x.append(y+z)
                if tokens[i] == "-":
                    x.append(z-y)
                if tokens[i] == "*":
                    x.append(y*z)
                if tokens[i] == "/":
                    x.append(z // y)
            else:
                x.append(int(tokens[i]))
        return x[0]



        
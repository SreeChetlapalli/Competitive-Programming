class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        x = []

        for i in range(len(tokens)):

            if tokens[i] == "+" or tokens[i] == "/" or tokens[i] == "*" or tokens[i] == "-":
                if len(x) == 2:
                    y = int(x.pop())
                    z = int(x.pop())
                if tokens[i] == "+":
                    x.append(y+z)
                if tokens[i] == "-":
                    x.append(z-y)
                if tokens[i] == "*":
                    x.append(y*z)
                if tokens[i] == "/":
                    x.append(z / y)
            else:
                x.append(tokens[i])
        return x[0]



        
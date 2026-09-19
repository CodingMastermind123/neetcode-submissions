class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        num1 = 0
        num2 = 0
        tempNum = 0

        for i in tokens:
            if (i != "+" and i != "-" and i != "*" and i != "/"):
                numStack.append(i)
            if (i == "+" or i == "-" or i == "*" or i == "/"):
                num1 = int(numStack[-1])
                num2 = int(numStack[-2])
                if i == "+":
                    tempNum = num2 + num1
                elif i == "-":
                    tempNum = num2 - num1
                elif i == "*":
                    tempNum = num2 * num1
                elif i == "/":
                    tempNum = int(num2 / num1)
                numStack.pop()
                numStack.pop()
                numStack.append(tempNum)
        
        result = int(numStack[0])

        return result
            

            
                
            
        
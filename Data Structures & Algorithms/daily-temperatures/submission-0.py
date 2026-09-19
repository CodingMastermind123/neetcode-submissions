class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(tempStack) != 0 and temperatures[i] > temperatures[tempStack[-1]]:
                index = tempStack.pop()
                result[index] = i - index
            tempStack.append(i)
        
        return result


        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        maxStack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while maxStack and temperatures[i] > maxStack[-1][0]:
                print(temperatures[i])
                curr, index = maxStack.pop()
                result[index] = i - index

            maxStack.append((temperatures[i], i))

        return result





        
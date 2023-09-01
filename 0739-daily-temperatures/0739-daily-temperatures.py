class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatureStack = []
        answer = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while temperatureStack and t > temperatureStack[-1][0]:
                currTemp, currIndex = temperatureStack.pop()
                answer[currIndex] = i - currIndex
            temperatureStack.append((t, i))
    
        
        return answer
        
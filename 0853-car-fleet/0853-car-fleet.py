class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionAndSpeed = []
        for i in range(len(position)):
            positionAndSpeed.append((position[i], speed[i]))
        
        positionAndSpeed.sort(reverse=True, key=lambda positionAndSpeed : positionAndSpeed[0])
        stack = []
        
        for curPosition, curSpeed in positionAndSpeed:
            timeTaken = (target - curPosition) / curSpeed
            stack.append(timeTaken)
            
            if len(stack) >= 2 and stack[-1] <= stack [-2]:
                stack.pop()
            
        return len(stack)
            
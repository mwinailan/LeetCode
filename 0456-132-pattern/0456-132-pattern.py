class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # [currNum, minNum]
        currMin = nums[0]
        
        for n in nums[1:]:
            # Case 1 : If n is greater or equal to the top of stack, pop the stack
            while stack and n >= stack[-1][0]:
                stack.pop()
            # CaSE 2 : iF n is smaller than the top of the stack and greater than the minimum value of the top of the stack, return True
            if stack and n > stack[-1][1]:
                return True
            # append the n to the stack
            stack.append([n, currMin])
            currMin = min(currMin, n)
        
        return False
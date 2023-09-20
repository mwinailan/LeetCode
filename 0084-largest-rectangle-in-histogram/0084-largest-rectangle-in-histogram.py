class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (start index, height)
        maxArea = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                startIndex, stackHeight = stack.pop()
                maxArea = max(maxArea, stackHeight * (i - startIndex))
                start = startIndex
            stack.append((start, height))
        
        for start, height in stack:
            maxArea = max(maxArea, height * (len(heights) - start))
        
        return maxArea
                
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastLetterIndex = {}
        for i, letter in enumerate(s):
            lastLetterIndex[letter] = i
        
        sizeOfParts = []
        sizeOfCurrentPart = currentLastIndex = 0
        
        for i, letter in enumerate(s):
            currentLastIndex = max(currentLastIndex, lastLetterIndex[letter])
            sizeOfCurrentPart += 1
            
            if i == currentLastIndex:
                sizeOfParts.append(sizeOfCurrentPart)
                sizeOfCurrentPart = 0
        
        return sizeOfParts
        
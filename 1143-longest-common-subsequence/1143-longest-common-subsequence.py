class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2d matrix
        lcsMatrix = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        
        # Start bottoms up approach
        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                #Case 1: text1 and text2 are the same
                if text2[i] == text1[j]:
                    lcsMatrix[i][j] = 1 + lcsMatrix[i+1][j+1]
                # Case 2:
                else:
                    lcsMatrix[i][j] = max(lcsMatrix[i+1][j], lcsMatrix[i][j+1])
        
        return lcsMatrix[0][0]
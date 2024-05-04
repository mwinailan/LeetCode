class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LIS = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    LIS[i][j] = 1 + LIS[i + 1][j + 1]
                else:
                    LIS[i][j] = max(LIS[i+1][j], LIS[i][j+1])
        
        return LIS[0][0]
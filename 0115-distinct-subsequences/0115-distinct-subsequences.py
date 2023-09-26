class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {} # (i,j) = res
        
        def findDistinctSubsequences(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i,j)] =  findDistinctSubsequences(i + 1, j) + findDistinctSubsequences(i + 1, j + 1)
            else:
                cache[(i,j)] = findDistinctSubsequences(i + 1, j)
            
            return cache[(i,j)]
        
        return findDistinctSubsequences(0,0)
            
                
            
        
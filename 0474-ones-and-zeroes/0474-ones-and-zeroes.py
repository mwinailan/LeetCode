class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        def findForms(i, m, n):
            if i == len(strs):
                return 0
            if (i,m,n) in dp:
                return dp[(i,m,n)]
            
            curM, curN = strs[i].count("0"), strs[i].count("1")
            dp[(i,m,n)] = findForms(i + 1, m, n)
            if m - curM >= 0 and n - curN >= 0:
                dp[(i,m,n)] = max(dp[(i,m,n)], 1 + findForms(i + 1, m - curM, n - curN))
            
            return dp[(i,m,n)]
        
        return findForms(0, m, n)
        
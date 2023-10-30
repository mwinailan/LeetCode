class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # store initial longest prefix
        longestPrefix = strs[0]
        
        # go through each str and compare to longestPrefix
        for i in range(1, len(strs)):
            tempLongestPrefix = ""
            curString = strs[i]
            
            for j in range(min(len(longestPrefix), len(curString))):
                if longestPrefix[j] != curString[j]:
                    break
                tempLongestPrefix += longestPrefix[j]
                
            # temp var = longestPrefix
            longestPrefix = tempLongestPrefix
        
        return longestPrefix
        
        
        
        
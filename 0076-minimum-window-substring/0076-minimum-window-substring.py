class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if t == "":
            return ""
        
        window, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        res, minResLen = [-1, -1], float("inf")
        left = 0
        matchingChars, needMatches = 0, len(countT)
        for right in range(len(s)):
            currentChar = s[right]
            window[currentChar] = 1 + window.get(currentChar, 0)
            
            if currentChar in countT and window[currentChar] == countT[currentChar]:
                matchingChars += 1
            
            while(matchingChars == needMatches):
                if (right - left + 1) < minResLen:
                    minResLen = right - left + 1
                    res = [left, right]
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    matchingChars -= 1
                left += 1
        
        if minResLen != float("inf"):
            l, r = res
            return s[l:r+1]
        else:
            return ""
            
            
            
        
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codeset = set()
        l, r = 0, k - 1
        
        while r <= len(s):
            codeset.add(s[l:r+1])
            l += 1
            r += 1
        print(codeset)
        return len(codeset) - 1 == 2 ** k
        
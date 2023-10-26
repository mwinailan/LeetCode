class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        l, r = 0, len(products) - 1
        
        for i in range(len(searchWord)):
            while l <= r and (len(products[l]) <= i or products[l][i] != searchWord[i]):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != searchWord[i]):
                r -= 1
            
            res.append([])
            windowLength = r - l + 1
            for j in range(min(3, windowLength)):
                res[-1].append(products[l + j])
            
        
        return res
        
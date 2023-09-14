from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        adjacencyList = {c : set() for w in words for c in w}
        res = []

        for j in range(len(words) - 1):
            w1, w2 = words[j], words[j+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            
            for i in range(minLength):
                if w1[i] != w2[i]:
                    adjacencyList[w1[i]].add(w2[i])
                    break

        # False = visited True = in path
        isVisited = {}

        def checkLetter(c):
            if c in isVisited:
                return isVisited[c]
            
            isVisited[c] = True
            for neighbor in adjacencyList[c]:
                if checkLetter(neighbor):
                    return True
            isVisited[c] = False
            res.append(c)

        
        for c in adjacencyList:
            if checkLetter(c):
                return ""
        
        res.reverse()
        return "".join(res)



            

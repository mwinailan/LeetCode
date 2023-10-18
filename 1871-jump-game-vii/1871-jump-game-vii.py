class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        farthest = 0
        
        while queue:
            i = queue.popleft()
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(len(s), i + maxJump + 1)):
                if s[j] == "0":
                    queue.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = i + maxJump
        
        return False
        
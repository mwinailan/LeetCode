class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gapsAtLocation = {0 : 0}
        
        for row in wall:
            position = 0
            for brick in row[:-1]:
                position += brick
                gapsAtLocation[position] = 1 + gapsAtLocation.get(position, 0)
        
        return len(wall) - max(gapsAtLocation.values())
import collections

from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        ROW, COLS = len(rooms), len(rooms[0])
        q = collections.deque()
        isVisited = set()

        for r in range(ROW):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    isVisited.add((r,c))
                    q.append([r,c])
        
        currDist = 0
        while q:
            for i in range(len(q)):
                currRow, currCol = q.popleft()
                rooms[currRow][currCol] = currDist

                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dx, dy in directions:
                    newRow = currRow + dx
                    newCol = currCol + dy

                    if newRow in range(ROW) and newCol in range(COLS) and (newRow, newCol) not in isVisited and rooms[newRow][newCol] != -1 and rooms[newRow][newCol] != 0:
                        isVisited.add((newRow,newCol))
                        q.append([newRow,newCol])
            currDist += 1



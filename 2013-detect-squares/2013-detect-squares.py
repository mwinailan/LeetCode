class DetectSquares:

    def __init__(self):
        self.coordinateCount = defaultdict(int) # (x,y) = count
        self.points = []
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.coordinateCount[(x, y)] += 1
        self.points.append([x,y])
        

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for px, py in self.points:
            if (abs(py - y) != abs(px - x)) or px == x or py == y :
                continue
            res += self.coordinateCount[(x,py)] * self.coordinateCount[(px,y)]
        
        return res
            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value,timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        keyAndTimeStamp = self.timeMap.get(key, [])
        
        for i in range(len(keyAndTimeStamp) - 1, -1, -1):
            if keyAndTimeStamp[i][1] <= timestamp:
                res = keyAndTimeStamp[i][0]
                break
                
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
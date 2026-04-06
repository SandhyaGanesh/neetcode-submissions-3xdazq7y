class TimeMap:

    def __init__(self):
        self.KVMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.KVMap:
            self.KVMap[key] = []
        self.KVMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.KVMap.get(key, [])
        if not values:
            return ""
        res = ""

        l = len(values)
        i = 0
        e = l - 1 

        while i <= e:
            m = (i + e)//2
            if timestamp < values[m][0]:
                e = m - 1
            elif timestamp > values[m][0]:
                res = values[m][1]
                i = m + 1
            else:
                return values[m][1]
        
        return res
        

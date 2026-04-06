class TimeMap:

    def __init__(self):
        self.moodMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        moodList = self.moodMap.get(key, [])
        moodList.append((value, timestamp))
        self.moodMap[key] = moodList

    def get(self, key: str, timestamp: int) -> str:
        moodList = self.moodMap.get(key, [])
        if not moodList:
            return ""
        l = 0
        r = len(moodList)
        mid = (l + r) // 2

        while l < r:
            mid = (l + r) // 2
            if moodList[mid][1] > timestamp:
                r = mid
            elif moodList[mid][1] < timestamp:
                l = mid + 1
            else:
                return moodList[mid][0]
       
        if moodList[mid][1] < timestamp:
            return moodList[mid][0]
        elif len(moodList) > mid - 1 > 0:
            return moodList[mid-1][0]
        else:
            return ""

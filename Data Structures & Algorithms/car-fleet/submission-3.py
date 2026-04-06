class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        numCars = len(position)
        newArr = []
        times = []
        for i in range(numCars):
            newArr.append((position[i], speed[i]))
        newArr.sort()

        for i in range(numCars - 1, -1, -1):
            
            t = (target - newArr[i][0]) / newArr[i][1]
            print(newArr[i][0], newArr[i][1], t)
            if times and times[-1] >= t:
                continue
            else:
                times.append(t)
        return len(times)

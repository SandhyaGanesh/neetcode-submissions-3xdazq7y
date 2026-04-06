class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = len(speed)
        posSpeed = [(position[i], speed[i]) for i in range(l)]
        posSpeed.sort(reverse=True)
        position = [posSpeed[i][0] for i in range(l)]
        speed = [posSpeed[i][1] for i in range(l)]

        fleetTime = -1
        res = 0
        for i in range(l):
            t = (target-position[i])/speed[i]
            if fleetTime < t:
                fleetTime = t
                res += 1

        return res
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = len(position)
        positionSpeed = [(position[i], speed[i]) for i in range(l)]
        positionSpeed.sort(reverse=True)
        tAhead = 0
        fleets = 0
        for p, s in positionSpeed:
            t = (target - p)/s
            if t <= tAhead:
                continue
            tAhead = t
            fleets += 1
        return fleets
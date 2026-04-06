class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = len(speed)
        posSpeed = [(position[i], speed[i]) for i in range(l)]
        posSpeed.sort(reverse=True)
        position = [posSpeed[i][0] for i in range(l)]
        speed = [posSpeed[i][1] for i in range(l)]

        stack = []
        res = 0
        for i in range(l):
            t = (target-position[i])/speed[i]
            if stack and stack[-1] >= t:
                continue
            stack.append(t)
            res += 1

        return res
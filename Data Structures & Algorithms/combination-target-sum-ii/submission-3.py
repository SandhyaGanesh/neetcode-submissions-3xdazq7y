class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(index, curr):
            if sum(curr) == target:
                c = curr.copy()
                res.append(tuple(c))
                return
            if index == len(candidates):
                return
            
            n = candidates[index]
            curr.append(n)
            helper(index + 1, curr)
            curr.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            helper(index + 1, curr)

        helper(0, [])
        res = [list(i) for i in set(res)]
        return res
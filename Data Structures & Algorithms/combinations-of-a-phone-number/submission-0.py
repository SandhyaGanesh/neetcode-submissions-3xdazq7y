class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digitMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []
        def helper(index, combination):
            nonlocal digitMap
            if len(combination) == len(digits):
                res.append(''.join(combination))
                return
            
            for letter in digitMap[digits[index]]:
                combination.append(letter)
                helper(index+1, combination)
                combination.pop()
        
        helper(0, [])
        return res
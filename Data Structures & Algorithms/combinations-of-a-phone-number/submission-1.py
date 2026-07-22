class Solution:
    def __init__(self):
        self.digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        resultCombinations = []
        l = len(digits)

        def recurse(i, combination):
            if i == len(digits):
                resultCombinations.append(combination)
                return
            
            for letter in self.digitMap[digits[i]]:
                recurse(i+1, combination + letter)
        
        recurse(0, "")
        return resultCombinations
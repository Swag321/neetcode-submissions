class Solution:
    def maxDepth(self, s: str) -> int:
        maxNest = 0
        counter = 0

        for p in s:
            if p == ")":
                counter -= 1
            elif p == "(":
                counter += 1
            
            maxNest = max(counter, maxNest)
        
        return maxNest
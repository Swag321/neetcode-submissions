class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # look at the index corresponding to element value
        # -1 -> 1 -> 3 -> 2 seen()
        
        for num in nums:
            if nums[abs(num)-1] < 0:
                return abs(num)
            else:
                nums[abs(num)-1] *= -1
        
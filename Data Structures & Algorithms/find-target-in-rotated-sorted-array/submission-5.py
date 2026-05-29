class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(logN) to find min/pivot point
        # Then look to left of pivot if > nums[-1] else look to right if < nums[-1]
        
        l,r = 0, len(nums) -1

        while l<r:

            m = (l+r)//2
            mE = nums[m]
            mR = nums[r]

            if mE < mR:
                r = m # lower the upper bound (include m)
            else:
                l = m+1 #increase the lower bound (skip m)
            
        pivotIndex = r

        if target > nums[-1]:
            l,r = 0,pivotIndex
        elif target < nums[-1]:
            l,r = pivotIndex, len(nums)-1
        else: #if target == nums[-1]
            return len(nums)-1 #index of target
        
        while l<r:
            m = (l+r)//2
            mE = nums[m]
            if target <= mE:
                r = m
            else:
                l = m+1
        
        if nums[r] == target:
            return r
        else:
            return -1
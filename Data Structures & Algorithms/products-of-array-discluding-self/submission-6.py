class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lNums = 1
        rNums = 1
        output = [1] * len(nums)

        for i in range(0,len(nums)):
            output[i] = lNums
            lNums *= nums[i]
            # next iteration will contain all left prods in lNums and output[i]
        
        for i in range(len(nums)-1,-1,-1):
            output[i] *= rNums
            rNums *= nums[i]
            # next iteration will contain all right prods in rNums and mult with all the left prods that are in output[i]

        return output
        

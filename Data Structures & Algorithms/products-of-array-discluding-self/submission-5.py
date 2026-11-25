class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lNums = [1] * len(nums)
        rNums = [1] * len(nums)

        for i in range(1,len(nums)):
            lNums[i] = lNums[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            rNums[i] = rNums[i+1] * nums[i+1]
        
        # print(lNums)
        # print(rNums)
        output = []

        for i in range(len(nums)):
            prod = lNums[i] * rNums[i]
            output.append(prod)

        return output

        # l: [1, 1, 2, 8]
        # r: [48, 24, 6, 1]
        # o: [48, 24, 12, 8]

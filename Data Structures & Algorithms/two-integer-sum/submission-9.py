class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complToInd =  {}
        
        for i in range(len(nums)):
            num = nums[i]
            # if current num is a compl then return associated i and current i
            if num in complToInd:
                return [complToInd[num], i]

            # otherwise calc compl and record associated i
            complToInd[target-num] = i
        


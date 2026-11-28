class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)

        output = []

        for i in range(len(nums)):
            l,r = i+1, len(nums)-1

            if i != 0 and nums[i] == nums[i-1]:
                # as long as its not first elem, skip if it was same as previous
                continue

            while l<r:
                triplets = [nums[i], nums[l], nums[r]]
                total = sum(triplets)
                if total <= 0:
                    if total == 0:
                        output.append(triplets)
                    l+=1
                    while l <= len(nums)-1 and nums[l] == nums[l-1]:
                        l += 1
                elif total > 0:
                    r -= 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1
                #edge cases?
        
        return output

        #[-4,-1,-1,0,1,2]
            

class Solution:
    def countElements(self, nums: List[int]) -> int:

        # Special Case
        if(len(nums) <= 2):
            return 0

        count = 0
        nums.sort()
        # print(nums)

        for i in range(len(nums)):
            if(nums[i] == nums[0]):
                count += 1
            # print(nums[::-1])
            if(nums[i] == nums[(len(nums) - 1)]):
                count += 1
        
        # print(count)

        # Special Case
        if((len(nums) - count) < 0):
            return 0
        
        return(len(nums) - count)



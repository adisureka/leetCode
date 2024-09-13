class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod_ = 1
        for i in range(len(nums)):
            prod_ *= nums[i]
        #print(prod_)

        if(prod_ > 0):
            return 1
        elif(prod_ == 0):
            return 0
        return -1

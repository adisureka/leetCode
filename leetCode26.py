class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        del_ele = 0
        k = 0
        pointer = 0

        while(pointer < len(nums)):
            if(pointer > 0 and nums[pointer] == nums[pointer - 1]):
                nums.pop(pointer)
            else:
                pointer += 1

        # for i in range(len(nums)):
        #     print(i)
        #     if(i > 0 and nums[i] == nums[i - 1]):
        #         # we cant use pop() when running a for loop as it shortens the list
        #         nums.pop(i)
        #         del_ele += 1
        print(nums)
        # print(del_ele)





        
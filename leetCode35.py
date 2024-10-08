class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        sp_index = 0
         
        # Using Binary Search as that is O(log n) complexity
        left = 0
        right =  len(nums) - 1
        middle = (left + right) // 2

        while (left <= right):
            if(nums[middle] == target):
                return middle
            elif(nums[middle] < target):
                if(middle + 1 < len(nums) and target < nums[middle + 1]):
                    return middle + 1 
                left = middle + 1
                middle = (left + right) // 2
            elif(nums[middle] > target):
                if(middle - 1 > 0 and target > nums[middle - 1]):
                    return middle
                right = middle - 1
                middle = (left + right) // 2
        if(nums[len(nums) - 1] < target):
            return len(nums)

        elif(nums[0] > target):
            return 0


        # for loop wont work here as it is O(n) complexity 
        # we must solve using O(log n)
        # for i in range(len(nums)):
        #     # if(nums[i] <)
        #     if (nums[i] == target):
        #         index = i
        #     elif(nums[i] != target and nums[i] > target):
        #         sp_index = i + 1
        #     elif(nums[i] != target and nums[i] < target):
        #         sp_index = i - 1
        #         print(sp_index)
        # return index
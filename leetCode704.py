class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Binary Search [Time Complexity: O(log n)]
        left = 0
        right = len(nums) - 1
        middle =  (left + right) // 2
        while(left <= right):
            if(nums[middle] == target):
                return middle
            elif(nums[middle] > target):
                right = middle - 1
                middle =  (left + right) // 2
            elif(nums[middle] < target):
                left = middle + 1
                middle = (left + right) //  2
        return - 1
            


        # Linear Search [Time Complexity: O(n)]
        # for i in range(len(nums)):
        #     if(nums[i] == target):
        #         return i
        # else: return -1
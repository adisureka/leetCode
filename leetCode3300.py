class Solution:
    def minElement(self, nums: List[int]) -> int:
        lst = []
        new_lst = []

        for i in range(len(nums)):
            # print(nums[i])
            lst.append(str(nums[i]))
        # print(lst)

        # Helper Function to help get the sum of an element in a list
        def strsum(nums:str):
            count = 0
            # Suppose nums = "123", loop through the stirng
            for i in range(len(nums)):
                digit = int(nums[i])
                count += digit
            return count
        
        for i in range(len(lst)):
            new_lst.append(strsum(lst[i]))
        
        print(new_lst)
        return(min(new_lst))
        # print(helper("123"))

        
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l1 = []
        count = 0

        # this works for even numbers we need for digits
        # for i in range(len(nums)):
            # if(nums[i]%2 == 0):
                # count += 1

        for i in range(len(nums)):
            l1.append(str(nums[i]))

        # print(l1)

        for i in range(len(l1)):
            if(len(l1[i]) % 2 == 0):
                count += 1
                print(l1[i])

        return(count)

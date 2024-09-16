class Solution:
    def findGCD(self, nums: List[int]) -> int:
        #first calculate the smallest number and the largest numebr in the array
        smallest = nums[0] # we do this to avoid silly mistakes by constraining the variable
        largest  = nums[0]

        '''
        # This works for other programming languages like Java and C
        for i in range(len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
            elif nums[i] > largest:
                largest = nums[i]
        #print(smallest, largest)
        '''

        smallest = min(nums)
        largest = max(nums)
        print(smallest, largest)

        gcd = 1
        for i in range(smallest, 0, -1):
            if largest % i == 0 and smallest % i == 0:
                gcd = i
                break

        return(gcd)
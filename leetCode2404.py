class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        nums.sort()
        # print(nums)

        lst = []

        count = Counter(nums)
        # print(count)

        val_max = 0

        for key in count:
            # remeber to check the key for odd numbers too
            if(count[key] > val_max and key % 2 == 0):
                val_max = count[key]  
        # print(val_max)

        for key in count:
            if(count[key] == val_max):
                lst.append(key)

        print(lst)
        lst.sort()

        for i in range(len(lst)):
            if(lst[i] % 2 == 0):
                return lst[i]
        else: return -1


        # This works for case 1 and is a quick fix
        # for i in range(len(nums)):
            # if(nums[i] % 2 == 0 and nums[i] != 0):
                # return nums[i]
        
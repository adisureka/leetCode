class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        # this is to ensure the length of nums is even
        if(len(nums) % 2 != 0):
            return False
        
        # this will return True as it is unordered
        # print({1,2} == {2,1})

        temp = Counter(nums)
        print(temp)

        # You cannot index a dicrionary
        # d = {"name":"Adi", "age":"26"}
        # print(d[0])

        # Keep in mind dictionary and set are unordered
        for key in temp:
            # print(key)
            value = temp[key]
            # print(value)
            if(value % 2 == 1):
                return False
        # we use for else thats why
        else: return True




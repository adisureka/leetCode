class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dict_ = {}
        for i in range(len(nums)):
            if(nums[i] not in dict_ ):
                dict_[nums[i]] = 1
            else:
                dict_[nums[i]] += 1
        adi = print
        adi(dict_)

        ans = []
        for key in dict_:
            if(dict_[key] > 1):
                ans.append(key)
        return(ans)


        # duplicate = []
        # lst = [5, 4, 3, 2]
        # lst.sort()
        # lst2 = sorted(lst)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if(nums[i] == nums[j] and i != j):
        #             duplicate.append(nums[i])
        # print(duplicate)
        # print(lst)
        # print(lst2)
        # print("id of list ", id(lst))
        # lst += [1]
        # print("id of list ", id(lst))
        # lst = lst + [1]
        # print("id of list ", id(lst))
        # print("Set version of the duplicate list ", set(duplicate))
        # return(duplicate) 

        
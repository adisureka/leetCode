# So basically they are saying that if key = n, raget should be n + 1
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        target = 0
        count  = 0
        lst = []

        for i in range(len(nums)):
            # easy quesion as the target is nums[i + 1]
            # if(i == key and nums[i + 1] == target):
            # this if is to assign the target
            target = nums[i]

            if(target == key and i + 1 < len(nums)):
                # print(target)
                lst.append(nums[i + 1])
        print(lst)
        
        lst = Counter(lst) 
        print(lst)

        maxi = (max(lst.values()))
            # this if is to count how many more times the target appears in the remainder of the list 
            # if(i > key and nums[i] == target):
                # count += 1
        print(maxi)

        for i in lst:
            value = lst[i]
            if(value == maxi):
                return i
                
        # print(count)

        return(target)
                

        
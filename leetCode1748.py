class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        lst = []
        temp = Counter(nums)
        print(temp)

        for key in temp:
            if(temp[key] < 2):
                lst.append(key)
    
        print(temp[2])
        print(set(temp))
        print(lst)
        return (sum(lst))
        
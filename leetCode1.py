class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] + nums[j] == target and i < j):
                    print(i,j)
                    print(nums[i], nums[j])
                    indice.append(i)
                    indice.append(j)
                    print("--------------")
        return indice
        
        
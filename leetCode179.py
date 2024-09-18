from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # Custom comparator function to compare two numbers as strings
        def compare(x, y):
            # Compare two possible combinations
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Convert each number to string
        nums_str = list(map(str, nums))
        
        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers
        largest_num = ''.join(nums_str)
        
        # Handle the edge case where all numbers are zero
        if largest_num[0] == '0':
            return '0'
        
        return largest_num

# Example usage
solution = Solution()
print(solution.largestNumber([10, 2]))  # Output: "210"
print(solution.largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"

'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        temp = min(nums)
        l1=[]

        # print(temp)
        for i in range(len(nums)):
            l1.append(str(nums[i]))
        # print(l1)
        temp1 = sorted(nums)
        # print(temp1[::-1])
        temp2 = sorted(l1)
        temp2= temp2[::-1]
        string = ""
        l0 = []

        # To check for the largest possibility
        # print("Temp 2 : ", temp2)
        for i in range(len(temp2)):
            if(temp2[i][-1] == "0"):
                # print("Temmp 2 in loop", temp2[i])
                l0.append(temp2[i])
            else:
                string += temp2[i]
        print(l0)

        if(len(l0) != 0):
            string += l0[0]
        
        # Passed 116 test cases but now they give nums = [111311, 1113]
        return(string)

'''

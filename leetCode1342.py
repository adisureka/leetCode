class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while(num != 0):
            if(num%2 == 0):
                num = num // 2
                # print("Even :", num)
                count += 1
            else: 
                num -= 1
                # print("Subtracted one:", num)
                count += 1
        return(count)

class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 1
        count = 0
        money = 0
        for i in range(n):
            # Ignore the first instance of i running from 0
            # run the modulus from 7 as 8th day is a new week and variable values must be reassigned
            if(i != 0 and i % 7 == 0):
                #print("If")
                monday += 1
                count = 0
            money += monday + count
            count += 1
            # print(money)
        return(money)

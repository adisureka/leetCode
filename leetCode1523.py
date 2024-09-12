class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """" Solution 1 Time Complexity: O(n)
        oddNum = 0
        for i in range(low, high+1):
            #print("Bug" , i)
            if(i%2)==1:
                oddNum +=1
        #print(oddNum)
        return oddNum
        """

        #Using time complexity O(1)

        oddNum = 0
        if(low%2)==1 and (high%2)==1:
            oddNum = (high - low) // 2 + 1
        elif(low%2)==0 and (high%2)==0:
            oddNum =(high - low) // 2
        elif(low%2)==1 and(high%2)==0:
            oddNum = (high - low) // 2 + 1 
        elif(low%2)==0 and(high%2)==1:
            oddNum = (high - low) // 2 + 1 
        #oddNum = (high - low) // 2 + 1
        #print(oddNum)
        return(oddNum)
    
    #Soemtimes stupid code is much faster as they have a faster algorithm which is O(1)
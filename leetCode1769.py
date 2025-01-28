class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        answer = []
        for i in range(len(boxes)):

            dist = 0

            for j in range(len(boxes)):
                if(j != i and int(boxes[j]) != 0):
                    temp = abs(j - i)
                    dist += temp
            answer.append(dist)
        print(dist)
        print(answer)

        return(answer)

            # if(int(boxes[i]) != 0):

                
            # elif(int(boxes[i]) == 1):
            #     print(1)
        
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split()
        l2 = s2.split()
        temp = []
        for i in range(len(l1)):
            # print(l1[i], "appears", l1.count(l1[i]))
            if(l1.count(l1[i]) == 1) and l1[i] not in l2:
                temp.append(l1[i])
        for i in range(len(l2)):
            # print(l2[i], "appears", l2.count(l2[i]))
            if(l2.count(l2[i]) == 1) and l2[i] not in l1:
                temp.append(l2[i])
        
        return(temp)


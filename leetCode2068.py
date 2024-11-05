class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        def count_letters(word:str):
            dic = Counter(word)
            return dic
        
        dic1 = count_letters(word1)
        dic2 = count_letters(word2)
        
        lst  = list(dic2.keys()) + list(dic1.keys())
        print(lst) # this list has both the keys from the 2 words

        for i in range(len(lst)):
        # maybe working cause of in built counter function
            if(abs(dic1[lst[i]] - dic2[lst[i]]) >= 4):
                return False
                # print("Here")
                # return True
        else:
            return True
                # print("In else")





        
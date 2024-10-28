class Solution:
    def equalFrequency(self, word: str) -> bool:
        lst = []
        print(Counter(word))
        for key in Counter(word):
            value = Counter(word)[key]
            lst.append(value)
        print(lst)
        lst.sort()
        print(lst)

        # if(len(set(lst)) == 1):
        #     return False

        def helper(lst):
            for i in range(len(lst)):
                if(lst[i] == 1):
                    temp = lst[0:i] + lst[i+1:]
                    print(temp)
                else:
                    temp = lst[0:i] + [lst[i] - 1] + lst[i+1:] 
                if(len(set(temp)) == 1):
                    return True
            else:
                return False
        
        # print(helper([1, 2 , 1]))
        return(helper(lst))
                
        # print(set(lst))




        
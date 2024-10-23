class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        lst = []
        most = 3
        count = 0
        for i in range(len(s)):
            # print(s[i: i+3])
            if(len(s[i:i+3]) == 3):
                lst.append(s[i:i+3])
        print(lst)
        # print(set(Counter(lst)))
        def match(sub:str):
            # sub = "yzz"
            temp = []
            for i in range(len(sub)):
                if(sub[i] not in temp):
                    temp.append(sub[i])
            # print(temp)
            if(len(sub) == len(temp)):
                return True
            else: return False

        for i in range(len(lst)):
            if(match(lst[i]) == True):
                count += 1
        
        return(count)
        

        
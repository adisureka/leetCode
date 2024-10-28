class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = Counter(arr)
        count = 0
        print(dic)
        my_set = set(arr)
        print(my_set)

        # Only hosts the values of the character that occurs once
        lst = []


        # Advances Set function
        for key in dic:
            value = dic[key]
            if(dic[key] == 1):
                count += 1
                lst.append(key)
        print(lst)

        if(k <= len(lst)):
            return lst[k-1]
        else:
            return ""

        # return(lst[k-1])

        # for i in range(len(arr)):
        #     if()
            # print(Counter(arr))
            # print(arr)
        
        
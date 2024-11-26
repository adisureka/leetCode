class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = []

        count =  Counter(s)
        print(count)

        for i in range(len(s)):

            if(s[i] in count and count[s[i]] == 1):
                lst.append(i)
                print(lst)
            else: print (-1)

        if(len(lst) == 0):
            return -1

        else: return lst[0]




        
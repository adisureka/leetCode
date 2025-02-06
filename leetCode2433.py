class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        lst = []
        
        for i in range(len(pref) - 1):
            lst.append(pref[i] ^ pref[i+1])
        print(lst)
        lst = [pref[0]] + lst

        return lst


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if(len(s1) != len(s2)):
            return False
        
        lst1 = []
        lst2 = []

        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                lst1.append(s1[i])
                lst2.append(s2[i])
        print(lst1)
        print(lst2)
        lst2.reverse()
        print(lst2)

        if(len(lst1) > 2):
            return False

        if(lst1 == lst2):
            return True
        else: return False
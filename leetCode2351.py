class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        lst = []
        count = 1
        # count = Counter(s)
        # print(count)

        for i in range(len(s)):
            # lst = lst.append(s[i])

            if(s[i] not in lst):
                lst.append(s[i])
                # count += 1
            else: return s[i]





            

        
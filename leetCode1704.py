class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        def count_vows(s):
            vows = ["a", "e", "i", "o", "u"]
            count = 0
            for i in range(len(s)):
                if(s[i].lower() in vows):
                    count += 1
            return count

        # how to divide a string by 2 is simply the len(string)//2
        mid = len(s)//2
        a = ""
        b = ""
        for i in range(mid):
            a += s[i]
        print(a)
        for i in range(mid, len(s)):
            b += s[i]
        print(b)

        print(count_vows(a))
        print(count_vows(b))

        if(count_vows(a) == count_vows(b)):
            return True
        else:
            return False
            

        
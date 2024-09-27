class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        a = False
        for i in range(x >= 1):
            new_string = string[::-1]
            print(new_string)
            if(new_string == string):
                a = True
            else: return False
        if(x == 0):
            a = True
        
        return(a)
    
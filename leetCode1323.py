class Solution:
    def maximum69Number (self, num: int) -> int:
        
        max_val = num
        strnum = str(num)
        # print(type(num))
        # print(type(strnum))
        newstr = ""
        replace = True

        for i in range(len(strnum)):
            if(strnum[i] == "9"):
                newstr += strnum[i]
            elif(strnum[i] == "6" and replace == True):
                newstr += "9"
                replace = False
            elif(strnum[i] == "6"):
                newstr += "6"

        return(int(newstr))
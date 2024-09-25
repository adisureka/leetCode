class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def containsNoZero(num):
            if(str(num).count("0") == 0):
                return True
            else: return False

        # convert every digit of n into a list to check if there is a '0'
        # print(repr(str(n)))
        # print(list(str(n)))
        # print(str(n).count("0"))

        c = []
        a = 1

        # if(str(n).count("0") == 0 or str(n).count("0") == 1):
        while True:
            b = n - a
            if(containsNoZero(b) and containsNoZero(a)):
                c = [a, b]
                print("Inside if: if you are here solution is working ", c)
                break
            else:
                a  += 1
            c = [a, b]
            print(c)
        return(c)

# try easier approaches using nested functions

'''
            # this works for 10
            if((str(b).count("0") == 1)):
                a += 1
                b = n - a
                c = [a , b]

            # find for 1010
            elif((str(b).count("0") == 2)):
                a = 11
                b = n - a
                # handle for 1057
                if(str(b).count("0") > 0):
                    a += 11
                    b = n - a
                    c = [a,b]

            elif(str(b).count("0") == 0):
                c = [a , b]
                break

        return(c)
'''

'''     
        if(n>3): 
            a = 2
            b = n - a
            c = [a, b]
        # if(list(str(n)))
        elif(n == 2):
            a = 1
            b = 1
            c = [a, b]
        
        # to handle for n = 1010
        elif(str(n).count("0") >= 2):

        return(c)
        '''
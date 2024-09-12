class Solution:
    def subtractProductAndSum(self, n: int) -> int:      
# Redo of this problem
        sum_ = 0
        prod_ = 1

        #first we find the sum and the product of n 
        # remember the len function:
        # you can only apply len on string values so convert accoridngly
        for i in range(len(str(n))):
            sum_ += int(str(n)[i])
            prod_ *= int(str(n)[i])
        print(prod_)
        print(sum_)
        diff = prod_ - sum_
        return(diff)
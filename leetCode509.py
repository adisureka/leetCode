class Solution:
    def fib(self, n: int) -> int:
        fido = (n - 1) + (n - 2)
        fib_lst = []
        a, b = 0, 1

        # Base Cases
        if(n == 0):
            return 0
        if(n == 1):
            return 1

        for i in range(2, n + 1):
            a,b = b, a + b 
            # fido = (n - 1) + (n - 2)
            # fib_lst[i] = fib_lst.append(fido)
            # print(fido)
            # print(fib_lst)
        return b


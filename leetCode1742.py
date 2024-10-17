class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        def sum_balln(n):
            count = 0
            n = str(n)
            for i in range(len(n)):
                count += int(n[i])
            return count

        print(sum_balln(213))
        print(sum_balln(21399))

        temp_lst = []
        dict_ = {}

        for i in range(lowLimit, highLimit + 1):
            temp_lst.append(sum_balln(i))
        print(temp_lst)
        for i in range(lowLimit, highLimit + 1):
            if(sum_balln(i) not in dict_):
                dict_[sum_balln(i)] = 1
            else:
                dict_[sum_balln(i)] += 1
        print(dict_)

        my_max = 0
        for key in dict_:
            if(dict_[key] > my_max):
                my_max = dict_[key]

        return(my_max)
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # 2 initalizers afer which we loop through the array
        small = 9999
        large = 0

        # declaring a variable for an inner list
        for i in range(len(logs)):
            in_lst = logs[i]

            # there is no number smaller than 0 as year is all positive numbers
            if(in_lst[0] < small):
                small = in_lst[0]

            if(in_lst[1] > large):
                large = in_lst[1]
        
        # works for the first two cases
        print(in_lst)
        print(small)
        print(large)

        lst = []

        # loop through the range (large plus one as we need the last date too)
        for i in range(small,large + 1):
            # check the max population now
            count = 0
            # print(i)

            # checking who is alive in the given range
            for j in range(len(logs)):
                # there was a bug in the second condition of the if as I had done "i <= logs[j][1]"
                if(i >= logs[j][0] and i < logs[j][1]):
                    count += 1
            lst.append((i, count))

        print(lst)

        max_pop = 0

        # looping through the appended list
        for i in range(len(lst)):
            if(lst[i][1] > max_pop):
                max_pop = lst[i][1]
        print(max_pop)

        for i in range(len(lst)):
            if(lst[i][1] == max_pop):
                return lst[i][0]

        # failed on case 35: "Wrong Answer"
        # bug located in the nested loop









        
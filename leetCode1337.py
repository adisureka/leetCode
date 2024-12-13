import numpy as np

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        army = []

        # Counting the soldiers in the rows
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if(mat[i][j] == 1):
                    count += 1
            army.append(count)
        # print(army)

        # creating a function to handle the duplicates
        def argsort(lst):
            print(lst)
            sort = sorted(lst)
            print(sort)
            emplst = []

            for element in sort:
                for i in range(len(lst)):
                    if(lst[i] == element and i not in emplst):
                        emplst.append(i)
            return emplst

        # Finally worked!! - w/o using numpy
        return argsort(army)[:k]


        # lst = np.argsort(army)
        # print(lst)

        # # Troubleshooting forcase 23
        # templst = lst[:k]
        # numlst = []

        # for i in templst:
        #     numlst.append((army[i],i))

        # print(numlst)
        # return lst[:k].tolist()


        # # Storing the value of the weakest row
        # weak = min(army)
        # print(weak)

        # # getting the index of the weakest row
        # for i in range(len(army)):
        #     if(army[i] == weak):
        #         print(i)
        


        
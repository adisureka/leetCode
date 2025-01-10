import numpy as np
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        mat = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append((i,j))
            mat.append(temp)

       
        # Check if the matrix is created
        # print(mat)

        # matrix print
        for row in mat:
            print(row)

        dist_lst = []
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dist = (abs(rCenter - mat[i][j][0]) + abs(cCenter - mat[i][j][1]))
                # print(dist)
                dist_lst.append(dist)
        # print(dist_lst)
        
        # dist_lst.sort()
        # print(dist_lst)

        # Usint numpy you can save the index's of the list
        index_lst = np.argsort(dist_lst)
        print(index_lst)

        # now apply the index list to the matrix you have created
        result = []

        for num in index_lst:
            # Typecast back to int as numpy uses int64 and not int
            # result.append((int(num // len(mat)), int(num % len(mat[0]))))
            result.append((int(num // len(mat[0])), int(num % len(mat[0]))))
            # print(result)


        return(result)
        
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        # Function to create list of max row values
        def max_r(List):
            temp = []
            for i in range(len(List)):
                temp.append(max(List[i]))
            return temp

        # Function to create list of max column values
        def mac_c(List):
            temp = []
            for j in range(len(List)):
                col1 =[]
                for i in range(len(List)):
                    col1.append(List[i][j])
                temp.append(max(col1))
            return temp

        print(mac_c(grid))
        print(max_r(grid))

        matrix = []

        # tempr = ([0] * len(grid[0])).copy()

        # Creating an empty new matrix
        for i in range(len(grid)):
            tempr = []
            for j in range(len(grid[0])):
                tempr.append(0)
            matrix.append(tempr)

        # Creating the ideal skyline as per guidelines
        for i in range(len(grid)):
            for j in range(len(grid)):
                matrix[i][j] = min(mac_c(grid)[j], max_r(grid)[i])

        # matrix[0][0] = 5
        # print(matrix)

        # for pylst in matrix:
        #     # print(pylst)
        #     for entry in pylst:
        #         entry = 999
        #         print(entry)
        #     print("-----------------")

        result = 0
        print(matrix)

        # Calculating the differences in each cell between given matrix and ideal matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result += matrix[i][j] - grid[i][j]

        return result
        
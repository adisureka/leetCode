class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt = [] # Triangle List
        for row in range(numRows):
            new_row = [1] * (row + 1)

            for col in range(1, row):
                new_row[col] = pt[row - 1][col - 1] + pt[row - 1][col]

            pt.append(new_row)
            
        return pt
        
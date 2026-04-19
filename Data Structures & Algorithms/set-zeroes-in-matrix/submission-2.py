class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # need a copy cuz if we replace 1 with 0 directly, it will afftect our decision for next one

        rowLen, colLen = len(matrix), len(matrix[0])
        colZero, rowZero = [False] * colLen, [False] * rowLen

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowZero[i] = True
                    colZero[j] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rowZero[i] == True or colZero[j] == True:
                    matrix[i][j] = 0

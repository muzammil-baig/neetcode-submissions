class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                #print(matrix[row][col])
                if matrix[row][col] == target:
                    return True
        return False
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
    
    # Create a result matrix of same size
        result = [[0] * n for _ in range(n)]
    
    # Use mapping rule to place each element
        for i in range(n):
            for j in range(n):
                new_row = j
                new_col = n - 1 - i
                result[new_row][new_col] = matrix[i][j]
    
    # Copy the result back to original matrix
        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]
        
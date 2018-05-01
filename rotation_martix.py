class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        import copy
        tmp = copy.deepcopy(matrix)
        l_matrix = len(matrix)
        for i in range(l_matrix):
            for j in range(l_matrix):
                matrix[i][j] = tmp[l_matrix - j - 1][i]
        # matrix[:] = zip(*matrix[::-1])
matrix = [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ]
Solution().rotate(matrix)
print(matrix)

int(10).bit_length()

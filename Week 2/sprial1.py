#https://leetcode.com/problems/spiral-matrix/
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        min_r, max_r = 0, m-1   # boundaries for row
        min_c, max_c = 0, n-1   # boundaries for column
        r, c = 0, 0             # initial indexed
        direction = 'Right'     # initial direction (R-D-L-U)

        ans = []
        for _ in range(m*n):
            ans.append(matrix[r][c])

            if direction == 'Right':
                if c == max_c:
                    r += 1
                    min_r += 1
                    direction = 'Down'
                else:
                    c += 1

            elif direction == 'Down':
                if r == max_r:          
                    c -= 1
                    max_c -= 1
                    direction = 'Left'
                else:
                    r += 1

            elif direction == 'Left':
                if c == min_c:
                    max_r -= 1
                    r -= 1
                    direction = 'Up'
                else:
                    c -= 1

            elif direction == 'Up':
                if r == min_r:
                    min_c += 1
                    c += 1
                    direction = 'Right'
                else:
                    r -= 1

        return ans
# Time Complexity : o(mn)
# Space Complexity : o(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # modify the array in place, with the minimum of the sum of the current element with 
        # the elements in the next row with atmost one column difference and return the minimum
        # in the first row
        for i in range(m-2,-1,-1):
            for j in range(n-1,-1,-1):
                if j==0:
                    matrix[i][j] = min( matrix[i][j]+matrix[i+1][j],matrix[i][j]+ matrix[i+1][j+1])
                elif j==n-1:
                     matrix[i][j] =min( matrix[i][j]+matrix[i+1][j], matrix[i][j]+matrix[i+1][j-1])
                else:
                     matrix[i][j] = min(matrix[i][j]+ matrix[i+1][j] , matrix[i][j]+matrix[i+1][j-1],matrix[i][j]+matrix[i+1][j+1])
        ans = matrix[0][0]
        for i in range(0,n):
            ans = min(ans,matrix[0][i])
        return ans

                

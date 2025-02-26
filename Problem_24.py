# Time Complexity : o(mn)
# Space Complexity : o(mn)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : was little confused about accessing
# coins array as we need to access i-1 th element

# Your code here along with comments explaining your approach
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        n = amount
        arr = [[0 for i in range(n+1)] for i in range(m+1)]
        arr[0][0]=1
        for i in range(1,m+1):
            for j in range(n+1):
                if j < coins[i-1]:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-coins[i-1]]
        return arr[m][n]

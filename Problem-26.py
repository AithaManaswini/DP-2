# Time Complexity : o(max(max(nums), len(nums)))
# Space Complexity : o(max(nums))
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# create a new array with the indices as the numbers in the array to bring
# it to the form of house robber as the problem says when we use nums[i], we cant
# use nums[i]+1, nums[i]-1.So, create an array with indices as nums.Then solve
# using house robber problem
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = [0 for i in range(max(nums)+1)]
        for i in range(len(nums)):
            d[nums[i]] += nums[i]   
        a = 0
        b = 0 
        print(d)   
        for i in d:
            x = max(b,a + i)
            a = b
            b = x
        return b

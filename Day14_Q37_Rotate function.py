class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        maxs = 0
        s = 0
        
        n = len(nums)
        for i in range(n):
            s+=nums[i]*i
        
        maxs = s
        ts = sum(nums)

        for i in range(1,n):
            s+= ts - n*nums[n-i]
            maxs = max(s,maxs)
        return maxs

            
        
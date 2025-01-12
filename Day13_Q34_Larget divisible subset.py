class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if not nums:
            return []
        
        nums.sort()

        l = [[num] for num in nums]

        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(l[i]) < len(l[j]) +1:
                    l[i] = l[j] + [nums[i]]

        return max(l,key = len)
        
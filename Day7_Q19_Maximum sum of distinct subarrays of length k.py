import itertools
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = set()
        sums = 0
        maxs = 0
        j = 0
        n = len(nums)

        for i in range(n):
            while nums[i] in s:
                sums -=  nums[j]
                
                s.remove(nums[j])
                j+=1

            s.add(nums[i])
            sums+=nums[i]

            if len(s) == k:
                maxs = max(maxs,sums)
                sums -= nums[j]
                s.remove(nums[j])
                j+=1
        return maxs

   
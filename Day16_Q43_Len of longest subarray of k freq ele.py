class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxl = 0
        l = 0
        d = defaultdict(int)

        for r in range(len(nums)):
            d[nums[r]]+=1

            while d[nums[r]]>k:
                d[nums[l]] -=1
                l+=1
            maxl = max(maxl,r-l+1)
        return maxl
            



                
        
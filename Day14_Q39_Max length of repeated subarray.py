class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        maxl = 0

        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    t = dp[i][j] + 1
                    dp[i+1][j+1] = t
                    maxl = max(t,maxl)
        return maxl
      
        
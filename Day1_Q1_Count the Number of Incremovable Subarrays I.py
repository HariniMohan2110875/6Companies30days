class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
    
        n = len(nums)
        left = 0

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                left += 1
            else:
                break

        if left == n - 1:
            ans = (n * (n + 1)) // 2
            return ans

        right = n - 1

        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                right -= 1
            else:
                break

        c = 0
        c += (n - right) + 1

        l = 0
        r = right

        while l <= left:
            while r < n and nums[l] >= nums[r]:
                r += 1
            c += (n - r + 1)
            l += 1

        return c
        
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = nums[n//2]
        moves = 0
        for num in nums:
            moves += abs(num - m)
        return moves
        
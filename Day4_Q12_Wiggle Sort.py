class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = sorted(nums)
        # Sort the array first
        n = len(nums)
        
        mid = (n+1)//2
        j = mid-1
        k = n-1

        for i in range(n):
            if i%2 == 0:
                nums[i] = l[j]
                j-=1
            else:
                nums[i] = l[k]
                k-=1
        nums = l

import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # while len(nums)>k:
        #     nums.remove(min(nums))
        
        # return nums
        h = []
        for ind,num in enumerate(nums):
            if(len(h)<k):
                heapq.heappush(h,(num,ind))
            else:
                heapq.heappushpop(h,(num,ind))
        
        return [v1 for v1,ind1 in sorted(h,key = lambda x:x[1])]

        # ordered = sorted((v,i) for i,v in enumerate(nums))[-k:]
        # return [v for v,_ in sorted(ordered, key=lambda x: x[1])]





        
            

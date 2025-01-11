class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # c =0 
        # l = []
        # nums.sort()
   
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if abs(nums[i]- nums[j]) ==k:
        #             l.append((nums[i],nums[j]))
        # l = set(l)
        # return len(l)
        c = 0
        f = Counter(nums)
        for key,val in f.items():
            if k ==0:
                if val>1:
                    c+=1
            
            elif(key+k) in f:
                c+=1
            
        return c
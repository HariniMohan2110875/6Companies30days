class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        
        for query in queries:
            k, trim = query
            l = []
            
            for idx, num in enumerate(nums):
                s = num[len(num)-trim:]  
                l.append((int(s), idx))  

            l.sort(key=lambda x: (x[0], x[1]))
            
            res.append(l[k-1][1])

        return res

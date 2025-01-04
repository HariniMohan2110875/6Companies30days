class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        res = []

        for _,h in envelopes:
            l = 0
            r = len(res) - 1

            while l<=r:
                mid = (l+r)//2
                if res[mid]>=h:
                    r = mid - 1
                else:
                    l = mid+1
                
            ind = l
            if ind == len(res):
                res.append(h)
            else:
                res[ind] = h
        return len(res)

        return c

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        b = [-inf]*(k+1)
        s = [0]*(k+1)
        for p in prices:
            for i in range(1,k+1):
                b[i] = max(b[i],s[i-1]-p)
                s[i] = max(s[i],b[i]+p)
        return s[-1]

 
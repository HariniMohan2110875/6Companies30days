class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def rec(x,jump,down):
            
            if x > k+1 :
                return 0
            ans = 0
            
            if x ==k: 
                ans+=1
            ans+= rec(x+pow(2,jump),jump+1,False)

            if not down and x:
                ans+= rec(x-1,jump,True)
            
            return ans

        return rec(1,0,False)
        
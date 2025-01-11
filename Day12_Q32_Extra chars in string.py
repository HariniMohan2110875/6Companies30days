class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # n = len(s)
        # d = set(dictionary)
        # dp = [0]*(n+1)

        # for i in range(n-1,-1,-1):
        #     dp[i] = dp[i+1] +1
        #     for j in range(i,n):
        #         subs = s[i:j+1]
        #         if subs in d:
        #             dp[i] = min(dp[i],dp[j+1])  

        # return dp[0]

        
        @cache
        def f(i):
            if i<len(s):
                res = 1 + f(i+1)

                for d in dictionary:
                    if s[i:].startswith(d):
                        res = min(res,f(i+len(d)))
                
                return (res)



            return 0
        
        return f(0)


        
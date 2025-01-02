class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # l = list(nums for nums in range(1,n+1))
        # i = 0
        # while(len(l)>1):
        #     i = (i+k-1)%len(l)
            
        #     print(i)
        #     l.pop(i)
        #     print(l)

        # return l[0]

        w = 0
        for i in range(2,n+1):
            w = (w+k)%i
        return w+1
        
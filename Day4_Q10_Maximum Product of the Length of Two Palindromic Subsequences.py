class Solution:
    def pali(self,s,bitm):
       # print(s)
        subs = ''.join(s[i] for i in range(len(s)) if (bitm & (1<<i)) > 0 )
        print(subs)
        if subs == subs[::-1]:
            return 1 
        else:
            return 0   
    def maxProduct(self, s: str) -> int:
        l = []
        n = len(s)
        for bitm in range(1,1 << n):
            if self.pali(s,bitm) == 1:
                l.append(bitm)
        print(l)
        maxp = 0
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i] & l[j] == 0:
                    l1 = bin(l[i]).count('1')
                    l2 = bin(l[j]).count('1')
                    maxp = max(maxp,l1*l2)
        return maxp
            
        

        
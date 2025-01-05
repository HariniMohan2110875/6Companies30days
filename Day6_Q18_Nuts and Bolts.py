#User function Template for python3
class Solution:

    def matchPairs(self, n, nuts, bolts):
        # code here
        order=['!','#','$','%','&','*','?','@','^']
        a=[]
        b=[]
        for i in order:
            if i in nuts:
                a.append(i)
        nuts.clear()
        nuts+=a
        for i in order:
            if i in bolts:
                b.append(i)
        bolts.clear()
        bolts+=b
        

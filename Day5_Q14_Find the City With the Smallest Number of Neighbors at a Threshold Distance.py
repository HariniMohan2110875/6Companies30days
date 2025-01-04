class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        d = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        
        for n1,n2,e in edges:
            d[n1][n2] = d[n2][n1] = e
        
        res = None
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    d[j][k] = min(d[j][k], d[j][i]+d[i][k])
        
        small = n
        

        for i in range(n):
            sc = 0
            for j in range(n):

                if d[i][j] <=distanceThreshold:
                    sc+=1
                
            if sc<=small:
                small = sc
                res = i
            
        return res

        
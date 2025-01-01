from copy import deepcopy
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = deepcopy(img)
        r = len(img)
        c = len(img[0])
        

        for x in range(r):
            for y in range(c):
                n = [img[i][j] for i in (x-1,x,x+1) for j in (y-1,y,y+1) 
                if 0<=i <r and 0<=j<c]
                ans[x][y] = sum(n)//len(n)
        return ans
        
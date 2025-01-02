class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x2<= xCenter:
            xc = x2
        elif x1<=xCenter:
            xc = x1
        else:
            xc = xCenter
        
        if y2<= yCenter:
            yc = y2
        elif y1<=yCenter:
            yc = y1
        else:
            yc = yCenter
        
        d = ((xc - xCenter)**2 - (yc - yCenter)**2)**0.5
        if d<=radius:
            return True
        else:
            return False
        
        

        
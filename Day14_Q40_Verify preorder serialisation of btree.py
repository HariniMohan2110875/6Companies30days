class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        degree = 1

        for node in preorder.split(","):
            degree -=1

            if degree<0:
                return False
            
            if node!="#":
                degree +=2

            
        if degree ==0:
            return True
        else:
            return False
        
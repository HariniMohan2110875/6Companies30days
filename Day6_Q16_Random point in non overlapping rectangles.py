class Solution:

        def __init__(self, rects: List[List[int]]):
            self.rects = rects
            self.points = []

            for rect in rects:
                self.points.append((rect[2] - rect[0] +1)* (rect[3]-rect[1] +1))
            self.total = sum(self.points)

            for i in range(1,len(self.points)):
                self.points[i] += self.points[i-1]
            self.points = [0] +self.points
            

        def pick(self) -> List[int]:
            
            ind = bisect.bisect_left(self.points,random.randint(1,self.total))
            rect = self.rects[ind-1]

            return [random.randint(rect[0],rect[2]),random.randint(rect[1],rect[3])]

            


    # Your Solution object will be instantiated and called as such:
    # obj = Solution(rects)
    # param_1 = obj.pick()
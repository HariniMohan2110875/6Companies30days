class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = 0
        arr2.sort()
        for i in range(len(arr1)):
            flag = 0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d:
                    flag = 1
            if flag ==0: c+=1
        return c
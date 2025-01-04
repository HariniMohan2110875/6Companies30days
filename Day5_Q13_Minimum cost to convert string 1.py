class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        c = 0
        arr = [[float('inf')] *26 for _ in range(26)]
        for i in range(26):
            arr[i][i] = 0

        for i in range(len(original)):
            v1 = ord(original[i]) - ord('a')
            v2 = ord(changed[i]) - ord('a')

            arr[v1][v2] = min(arr[v1][v2],cost[i])
        
        for i in range(26):
            for j in range(26):
                    for k in range(26):
                        arr[j][k] = min(arr[j][k],arr[j][i]+arr[i][k])
        
        for i in range(len(source)):
            v1 = ord(source[i]) - ord('a')
            v2 = ord(target[i]) - ord('a')
            
            if v1 == v2:
                continue
            if arr[v1][v2] == float('inf'):
                return -1
            
            c+=arr[v1][v2]





        return c
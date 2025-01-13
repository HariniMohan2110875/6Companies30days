class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        n = len(g)
        c = len(s)
        cnt = 0
        g.sort()
        s.sort()
        i = j = 0

        while i < n and j < c:
            if g[i] <= s[j]:
                cnt+=1
                i+=1
            j+=1
        return cnt

        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        mins = 0

        while q and fresh>0:
            for _ in range(len(q)):
                x,y = q.popleft()

                for dx,dy in d:
                    nx,ny = x+dx, y+dy

                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -=1
                        q.append((nx,ny))
            mins+=1

        if fresh == 0:
            return mins
        else:
            return -1

            
        
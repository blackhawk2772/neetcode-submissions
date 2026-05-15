class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n= len(grid[0])
        
        q = deque()
        #visited = set()
        hFruits = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hFruits += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        minutes = 0
        directions = [1,0], [-1,0], [0,1], [0,-1]

        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dr,dl in directions:
                    posx = x + dr
                    posy = y + dl
                    if posx >= 0 and posy >= 0 and posx < m and posy < n and grid[posx][posy] == 1 and grid[posx][posy] != -1:
                        hFruits -= 1
                        q.append([posx,posy])
                        grid[posx][posy] = -1
            minutes += 1
        
        if hFruits > 0:
            return -1
        else:
            return max(0,minutes-1)

                    

                


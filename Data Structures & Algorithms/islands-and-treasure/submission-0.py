class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m = len(grid)
        n = len(grid[0])

        visited = set()
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visited.add((i,j))

        dist = 0
        
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                grid[x][y] = dist
                
                directions = [1,0],[-1,0], [0,1], [0,-1]
                for dr, dl in directions:
                    posx = x + dr
                    posy = y + dl
                    if posx >= 0 and posy >= 0 and posx<m and posy < n and grid[posx][posy] != -1 and (posx,posy) not in visited:
                        q.append([posx,posy])
                        visited.add((posx,posy))
            dist += 1
                    
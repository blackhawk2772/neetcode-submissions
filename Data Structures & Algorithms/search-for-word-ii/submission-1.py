class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        M,N = len(board), len(board[0])
        
        trie = {}

        res = set()

        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word
        
        visited = set()
        
        def dfs(x, y, node):

            if "$" in node:
                res.add(node["$"]) 
            
            directions = [1,0], [-1,0], [0,1], [0,-1]
            visited.add((x,y))
            for dr,dl in directions:
                posx = x + dr
                posy = y + dl
                if posx >= 0 and posx < M and posy >= 0 and posy < N:
                    if board[posx][posy] in node and ((posx,posy) not in visited):
                        dfs(posx, posy, node[board[posx][posy]])
            visited.remove((x,y))

            return

        for i in range(M):
            for j in range(N):
                if board[i][j] in trie:
                    dfs(i,j, trie[board[i][j]])

        return list(res)
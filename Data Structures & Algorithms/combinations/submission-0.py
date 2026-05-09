class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        self.res = [] 
        self.dfs(n,k,1,[])

        return self.res    
        # range = 1...n
        # combinations of k numbers

    def dfs(self, n, k, i, cur):

        if i > n + 1 or k-len(cur) > n - i + 1:
            return
        
        if len(cur) == k:
            self.res.append(cur.copy())
            return cur
        
        cur.append(i)
        self.dfs(n,k,i+1,cur)

        cur.pop()
        self.dfs(n,k,i+1,cur)
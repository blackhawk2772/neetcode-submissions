class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.endOfWord = True

    def dfs(self, node, word):
        if not word:
            return node.endOfWord
        
        ch = word[0]
        if ch == '.':
            for child in node.children.values():
                if self.dfs(child, word[1:]):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self.dfs(node.children[ch], word[1:])

    def search(self, word: str) -> bool:
        cur = self.root

        return self.dfs(cur, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
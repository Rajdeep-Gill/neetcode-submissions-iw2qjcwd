class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]

        curr.end = True
        

    def search(self, word: str) -> bool:
        # if we have a dot, we recurisvely call with all possibilities. return true if found
        curr = self.root
        def dfs(new_root, i):
            if i == len(word):
                return new_root.end

            if word[i] == ".":
                ans = False
                for j in range(26):
                    if new_root.children[j] != None:
                        ans = ans or dfs(new_root.children[j], i+1)
                return ans
            else:
                idx = ord(word[i]) - ord('a')
                if new_root.children[idx] != None:
                    return dfs(new_root.children[idx], i+1)
                else:
                    return False

        return dfs(curr, 0)




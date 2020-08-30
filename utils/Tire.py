# trie
# search, insert, get word counts
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        if 'count' not in cur:
            cur['count'] = 1
        else:
            cur['count'] = cur['count'] + 1

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            else:
                cur = cur[c]
        if "count" in cur:
            return True
        return False

    def startWith(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    trie.insert("water")
    trie.insert("water")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startWith("app"))
    print(trie.root)


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        if 'cnt' not in cur:
            cur['cnt'] = 1
        else:
            cur['cnt'] = cur['cnt'] + 1

    def startWith(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return 0
            cur = cur[c]
        if 'count' not in cur:
            return 1
        else:
            return 2

class Solution:
    def findWords(self, words, board):
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            if "cnt" not in cur:
                cur["cnt"] = 1
            else:
                cur["cnt"] = cur["cnt"] + 1
        def dfs(i, j, c, cur, cur_str):
            if c not in cur:
                return
            cur = cur[c]
            cur_str = cur_str + c
            board[i][j]= "#"
            if "cnt" in cur:
                self.res.append(cur_str)
            four_loc = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            for x, y in four_loc:
                x, y =  i + x, j + y
                if x > self.row or x == self.row or y > self.col or y == self.col:
                    continue
                if board[x][y] == "#":
                    continue
                dfs(x, y, board[x][y], cur, cur_str)
                board[i][j] = c
        self.row = len(board)
        self.col = len(board[0])
        self.trie = trie
        word = []
        self.res = []
        for i in range(self.row):
            for j in range(self.col):
                cur_str = ""
                dfs(i, j, board[i][j], trie, cur_str)
                word.append(c)
        print(self.res)


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    # search all words exist in board
    # construct trie
    s = Solution()
    s.findWords(words, board)
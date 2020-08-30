from collections import deque

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = '*'
        self.right = '*'
    def __str__(self):
        return f'<{self.data}, {self.left}, {self.right}>'  # Py 3.6


def build_tree_breadth_first01():
    pass

def build_tree_breadth_frest02():
    n = iter(data)
    tree = Node(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            head.left = Node(next(n))
            fringe.append(head.left)
            head.right = Node(next(n))
            fringe.append(head.right)
        except StopIteration:
            break
    print(tree)


if __name__ == '__main__':
    data = [3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value 
class Tree():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add(value, self.root)
    
    def _add(self, value, node):
        if value < node.value:
            if node.left:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(value, node.right)
            else:
                node.right = Node(value)
    def find(self, value):
        if self.root:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif (value < node.value and node.left):
            self._find(value, node.left)
        elif (value > node.value and node.right):
            self._find(value, node.right)
def iter_pr(node=None):
    if not node:
        return
    lis = list()
    lis.append(node)
    while lis:
        node = lis.pop()
        visit(node)
        if node.right:
            lis.append(node.right)
        if node.left:
            lis.append(node.left)
def visit(node):
    print(node.value)
tree = Tree()
tree.add(5)
tree.add(2)
tree.add(9)
tree.add(7)
tree.add(3)
tree.add(1)
tree.add(4)
tree.add(10)
tree.add(18)
print("Итеративный обход дерева")
iter_pr(tree.root)
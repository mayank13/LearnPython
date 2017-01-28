from Tree import Node


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def addNode(self, root, node):
        if self.root is None:
            self.root = node
            return
        if root.leftNode is None:
            root.leftNode = node
            return
        elif root.rightNode is None:
            root.rightNode = node
            return

        else:
            self.addNode(root.leftNode, node)


    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.leftNode)
        self.preorder(root.rightNode)


bt = BinaryTree()
nodes = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(nodes)):
    bt.addNode(bt.root, Node(nodes[i]))
print('---Binary Tee---')
bt.preorder(bt.root)

class Node:
    """A simple Binary Node to be used in a Tree"""

    def __init__(self, value=-1, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

    def __str__(self):
        return ' Node value --> %s' % self.value


class Tree:
    """A Binary Tree """

    def __init__(self, root):
        self.root = root

    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.leftNode)
        self.preorder(root.rightNode)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.leftNode)
        print(root.value)
        self.inorder(root.rightNode)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.leftNode)
        self.postorder(root.rightNode)
        print(root.value)


nodeTest = Node()
print(nodeTest)
print(Node)
rootNode = Node(1)
tree = Tree(rootNode)

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

rootNode.leftNode = node2
rootNode.rightNode = node3
node2.leftNode = node4
node2.rightNode = node5
node3.leftNode = node6
node3.rightNode = node7
print('----Preorder----')
tree.preorder(rootNode)
print('----Inorder----')
tree.inorder(rootNode)
print('----Postorder----')
tree.postorder(rootNode)

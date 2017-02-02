from Tree import Node
from collections import deque


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.noOfLeftNodes = 0
        self.noOfRightNodes = 0

    def addNode(self, root, node):
        if self.root is None:
            self.root = node
            return
        if root.leftNode is None:
            root.leftNode = node
            self.noOfLeftNodes += 1
            return
        elif root.rightNode is None:
            root.rightNode = node
            self.noOfRightNodes += 1
            return

        else:
            if self.noOfLeftNodes - self.noOfRightNodes < 2:
                self.addNode(root.leftNode, node)
            else:
                self.addNode(root.rightNode, node)

    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.leftNode)
        self.preorder(root.rightNode)

    def levelorder(self, root):
        queue = deque([])
        queue.append(root)
        while queue:
            curr = queue.popleft()
            print(curr)
            if curr.leftNode:
                queue.append(curr.leftNode)
            if curr.rightNode:
                queue.append(curr.rightNode)

    def add_node_inorder(self, node):
        queue = deque([])
        if self.root is None:
            self.root = node
            return
        queue.append(self.root)
        curr_node = self.root
        while queue:
            curr_node = queue.popleft()
            if curr_node.leftNode is not None:
                queue.append(curr_node.leftNode)
            else:
                curr_node.leftNode = node
                return
            if curr_node.rightNode is not None:
                queue.append(curr_node.rightNode)
            else:
                curr_node.rightNode = node
                return
        return self.root


bt = BinaryTree()
nodes = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(nodes)):
    bt.addNode(bt.root, Node(nodes[i]))
print('---Binary Tee---')
bt.preorder(bt.root)

bt2 = BinaryTree()
bt2.add_node_inorder(Node(1))
bt2.add_node_inorder(Node(2))
bt2.add_node_inorder(Node(3))
bt2.add_node_inorder(Node(4))
bt2.add_node_inorder(Node(5))
bt2.add_node_inorder(Node(6))
bt2.add_node_inorder(Node(7))
print('---Pre Order Traversal---')
bt2.preorder(bt2.root)
print("***Level Order Traversal***")
bt2.levelorder(bt2.root)

# -- Queue Test --
# q2 = deque([1, 2, 3])
# print(q2.popleft())
# print(q2.popleft())
# print(q2.popleft())
# el = q2.popleft()
# print(el)

bt3 = BinaryTree()
bt3Nodes = [1, 2, 5, 3, 4, 6, 7]
for i in range(len(bt3Nodes)):
    bt3.add_node_inorder(Node(bt3Nodes[i]))
print("--Pre Order Traversal")
bt3.preorder(bt3.root)

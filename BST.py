class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)
    def _insert(self,data,curr_node):
        if data<curr_node.data:
            if curr_node.left is None:
                curr_node.left=Node(data)
            else:
                self._insert(data,curr_node.left)
        elif data>curr_node.data:
            if curr_node.right is None:
                curr_node.right=Node(data)
            else:
                self._insert(data,curr_node.right)
        else:
            print("Value is already present")
    def find(self,data):
        if self.root:
            isfound=self._find(data,self.root)
            if isfound:
                return True
            else:
                return False
        else:
            return False
    def _find(self,data,curr_n):
        if data>curr_n.data and curr_n.right:
            return self._find(data,curr_n.right)
        elif data<curr_n.data and curr_n.left:
            return self._find(data,curr_n.left)
        if data==curr_n.data:
            return True
tree=BST()
tree.insert(5)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(10)
tree.insert(9)
print(tree.find(10))

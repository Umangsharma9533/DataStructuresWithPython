class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)
    def printTree(self,inp):
        if inp=="preorder":
            return self.preorder_print(tree.root,"")
        elif inp=="inorder":
            return self.inorder_print(tree.root,"")
        elif inp=="postorder":
            return self.postorder_print(tree.root,"")
        elif inp=="levelorder":
            return self.levelorder_print(tree.root,"")
        elif inp=="reverse_levelorder":
            tarve=self.levelorder_print(tree.root,"")
            return tarve[::-1]
        else:
            print("Enter valid input,i.e. : preorder,inorder or postorder")
            return
    def preorder_print(self,start,traversal):
        if start:
            traversal+=(str(start.value)+"->")
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal
    def inorder_print(self,start,traversal):
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=(str(start.value)+"->")
            traversal=self.inorder_print(start.right,traversal)
        return traversal
    def postorder_print(self,start,traversal):
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal=self.postorder_print(start.right,traversal)
            traversal+=(str(start.value)+"->")
        return traversal
    def levelorder_print(self,start,taversal):
        if not start:
            return
        queue=[]
        queue.append(start)
        traversal=""
        while(len(queue)>0):
            node=queue.pop(0)
            traversal+=(str(node.value)+"->")
            if node.left :
                queue.append(node.left)
            if node.right :
                queue.append(node.right)
        return traversal
    def height_Tree(self,start):
        if start is None:
            return -1
        left_height=self.height_Tree(start.left)
        right_height=self.height_Tree(start.right)
        return 1+max(left_height,right_height)
    def size_Tree(self,start):
        if start is None:
            return 0
        return 1+self.size_Tree(start.left)+self.size_Tree(start.right)
tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
print(tree.printTree("reverse_levelorder"))
print(tree.height_Tree(tree.root))
print(tree.size_Tree(tree.root))

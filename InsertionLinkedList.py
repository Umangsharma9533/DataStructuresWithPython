#Creating a New Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Creating a Linkedlist
#Class contain 5 Functions:
#__init__(): It acts a constructor , initialize a head for a linkedlist
# print_linkedlist() : Print the complete linkedlist
# prepend() : appending a node in front of a linked list head
# insertAfterNode() : Insert a node after particular node
# append() : will append a node at lasy of the linkedlist
#del_headNode(): will take a key/value and check whether that is head node a then delete it
class LinkedList:
    def __init__(self):
        self.head=None
    def print_linkedlist(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data,end=" ")
            print("->",end=" ")
            curr_node=curr_node.next
        print("NULL_PTR")
    def prepend(self,data):
        new_node=Node(data)
        curr=self.head
        new_node.next=self.head
        self.head=new_node
    def insertAfterNode(self,data,prev_node):
        if not prev_node:
            print("Prevnode is not present in the list")
            return
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        
        
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def del_Node(self,key):
        curr_node=self.head
        if curr_node and curr_node.data==key:
            self.head=curr_node.next
            curr_node.next=None
            return
        prev = None
        while curr_node and curr_node.data!=key :
            prev=curr_node
            curr_node=curr_node.next
        if curr_node is None:
            print("Node doesnt exist")
            return
        prev.next=curr_node.next
        curr_node.next= None
    def del_Node_AtPosition(self,position):
        curr_N=self.head
        index=0
        if position<0:
            print("Entered value below zero,enter valid input ")
            return
        if curr_N and index==position:
            self.head=curr_N.next
            curr_N.next=None
            return
        while curr_N and index!=position:
            prev_n=curr_N
            curr_N=prev_n.next
            index+=1
        if curr_N is None:
            print("Node doesn't exist")
            return
        prev_n.next=curr_N.next
        curr_N.next=None
    def length_llist_iter(self):
        count=0
        curr_N=self.head
        while curr_N:
            curr_N=curr_N.next
            count+=1
        return count    
    
    def length_llist_recursive(self,node):
        if node is None:
            return 0
        return 1+self.length_llist_recursive(node.next) 
#Creating a object of a linkedlist class
llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.prepend("O")
llist.insertAfterNode("M",llist.head.next)
llist.print_linkedlist()#Creating a New Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Creating a Linkedlist
#Class contain 5 Functions:
#__init__(): It acts a constructor , initialize a head for a linkedlist
# print_linkedlist() : Print the complete linkedlist
# prepend() : appending a node in front of a linked list head
# insertAfterNode() : Insert a node after particular node
# append() : will append a node at lasy of the linkedlist
#del_headNode(): will take a key/value and check whether that is head node a then delete it
class LinkedList:
    def __init__(self):
        self.head=None
    def print_linkedlist(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data,end=" ")
            print("->",end=" ")
            curr_node=curr_node.next
        print("NULL_PTR")
    def prepend(self,data):
        new_node=Node(data)
        curr=self.head
        new_node.next=self.head
        self.head=new_node
    def insertAfterNode(self,data,prev_node):
        if not prev_node:
            print("Prevnode is not present in the list")
            return
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        
        
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def del_Node(self,key):
        curr_node=self.head
        if curr_node and curr_node.data==key:
            self.head=curr_node.next
            curr_node.next=None
            return
        prev = None
        while curr_node and curr_node.data!=key :
            prev=curr_node
            curr_node=curr_node.next
        if curr_node is None:
            print("Node doesnt exist")
            return
        prev.next=curr_node.next
        curr_node.next= None
    def del_Node_AtPosition(self,position):
        curr_N=self.head
        index=0
        if position<0:
            print("Entered value below zero,enter valid input ")
            return
        if curr_N and index==position:
            self.head=curr_N.next
            curr_N.next=None
            return
        while curr_N and index!=position:
            prev_n=curr_N
            curr_N=prev_n.next
            index+=1
        if curr_N is None:
            print("Node doesn't exist")
            return
        prev_n.next=curr_N.next
        curr_N.next=None
    def length_llist_iter(self):
        count=0
        curr_N=self.head
        while curr_N:
            curr_N=curr_N.next
            count+=1
        return count    
    
    def length_llist_recursive(self,node):
        if node is None:
            return 0
        return 1+self.length_llist_recursive(node.next) 
#Creating a object of a linkedlist class
#Testing of the above code
# llist=LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.append("E")
# llist.prepend("O")
# llist.insertAfterNode("M",llist.head.next)
# llist.print_linkedlist()
# llist.del_Node_AtPosition(-5565)
# llist.print_linkedlist()

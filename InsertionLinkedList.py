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
#Creating a object of a linkedlist class
llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.prepend("O")
llist.insertAfterNode("M",llist.head.next)
llist.print_linkedlist()

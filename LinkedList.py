
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
    def mergeTwoSortedLinkedLists(self,llist):
        p=self.head
        q=llist.head
        s=None
        start=None
        if not p:
            return q
        if not q:
            return p
        if p.data > q.data:
            s=q
            q=s.next
            start=s
        else:
            s=p
            p=s.next
            start=s
        while p and q:
            if p.data < q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return start
    def removeDuplicateNodeInList(self):
        curr=self.head
        prev=None
        dict_values=dict()
        while curr:
            if curr.data in dict_values:
                prev.next=curr.next
                curr=None
            else:
                dict_values[curr.data]=1
                prev=curr
            curr=prev.next
    def removeNthNodeFromLast(self,loc):
        curr=self.head
        length=self.length_llist_iter()
        prev=None
        while curr :
            if length-loc==0:
                prev.next=curr.next
                curr=None
                return
            else:
                length-=1
                prev=curr
                curr=prev.next
        if not curr:
            print("Node out of bound or not found")
            return
    def countOccurancesIterative(self,data):
        curr=self.head
        count=0
        while curr:
            if curr.data==data:
                count+=1
            curr=curr.next
        return count
    def countOccurancesRecursive(self,node,data):
        if not node:
            return 0
        if node.data==data:
            return 1+ self.countOccurancesRecursive(node.next,data)
        else:
            return self.countOccurancesRecursive(node.next,data)
    def rotateSinglyLinkedList(self,rot_no):
        pt1=self.head
        pt2=self.head
        length=self.length_llist_iter()
        while pt1 and length-rot_no>0:
            prev=pt1
            pt1=pt1.next
            pt2=pt2.next
            length-=1
        pt1=prev
        while pt2:
            prev=pt2
            pt2=pt2.next
        pt2=prev
        pt2.next=self.head
        self.head=pt1.next
        pt1.next=None
    def isPalindrome(self):
        string=""
        ptr=self.head
        while ptr:
            string+=ptr.data
            ptr=ptr.next
# Check whether reverse and actual of string is same
        return string==string[::-1]
    def moveTailToHead(self):
        ptr=self.head
        prev=None
        while ptr.next:
            prev=ptr
            ptr=ptr.next
        ptr.next=self.head
        self.head=ptr
        prev.next=None
    def sumTwoLinkedLists(Self,llist):
        pass
#Creating a object of a linkedlist class
#Demo use of function in LinkedList class
llist1=LinkedList()
#llist2=LinkedList()
llist1.append("1")
llist1.append("B")
llist1.append("C")
llist1.append("D")
llist1.append("C")
llist1.append("B")
llist1.append("1")
#llist2.append(3)
#llist2.append(4)
#llist2.append(6)
#llist2.append(8)
llist1.print_linkedlist()#Creating a New Node
print(llist1.isPalindrome())
llist1.moveTailToHead()
llist1.print_linkedlist()
#llist1.removeNthNodeFromLast(2)
#llist1.print_linkedlist()
#print(llist1.countOccurancesIterative(4))
#print(llist1.countOccurancesRecursive(llist1.head,4))
#llist2.print_linkedlist()#Creating a New Node
#llist1.mergeTwoSortedLinkedLists(llist2)
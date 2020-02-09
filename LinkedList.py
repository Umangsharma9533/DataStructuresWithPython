
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
    def print_num(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data,end="")
            curr_node=curr_node.next
        print()
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
    def sumTwoLinkedLists(self,llist):
        p=self.head
        q=llist.head
        final_List=LinkedList()
        carry=0
        while p or q:
            if not p:
                i=0
            else:
                i=p.data
            if not q:
                j=0
            else:
                j=q.data
            s=i+j+carry
            if s>=10:
                remainder=s%10
                carry=1
                final_List.prepend(remainder)
            else:
                carry=0
                final_List.prepend(s)
            if p:
                p=p.next
            if q:
                q=q.next
        if carry==1:
            final_List.prepend(carry)
        final_List.print_num()
        
class CircularLinkedList:
    def __init__(self):
        self.head=None
    def print_linkedlist(self):
        curr_node=self.head
        while curr_node.next!=self.head:
            print(curr_node.data,end=" ")
            print("->",end=" ")
            curr_node=curr_node.next
        print(curr_node.data,end=" ")
        print("NULL_PTR")
    def prepend(self,data):
        new_node=Node(data)
        curr=self.head
        new_node.next=self.head
        if not self.head:
            new_node.next=new_node
        else:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            self.head=new_node
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            self.head.next=self.head
        else:
            curr=self.head
            new_node=Node(data)
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head
    def insertAfterNode(self,data,loc):
        if not self.head:
            self.head=Node(data)
            self.head.next=self.head
        else:
            curr=self.head
            new_node=Node(data)
            while loc>0:
                prev=curr
                curr=curr.next
                loc-=1
            prev.next=new_node
            new_node.next=curr
    def removeNode(self,loc):
        if loc==1:
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next=self.head.next
            self.head=cur.next
        else:
            curr=self.head
            while loc>1:
                prev=curr
                curr=curr.next
                loc-=1
            prev.next=curr.next
    def lengthCLinkedList(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
            if curr==self.head:
                break
        return count
    def splitCLinkedList(self):
        length=self.lengthCLinkedList()
        if length==0:
            return None
        if length==1:
            return self.head
        mid=length/2
        count=0
        prev=None
        curr=self.head
        while curr and count<mid:
            count+=1
            prev=curr
            curr=curr.next
        prev.next=self.head
        split_clist=CircularLinkedList()
        while curr.next!=self.head:
            split_clist.append(curr.data)
            curr=curr.next
        split_clist.append(curr.data)
        print("First half")
        self.print_linkedlist()
        print("Second half")
        split_clist.print_linkedlist()
#Creating a object of a linkedlist class
#Demo use of function in LinkedList class
# llist1=LinkedList()
# llist2=LinkedList()
# llist1.append(4)
# llist1.append(5)
# llist1.append(6)
# llist2.append(6)
# llist2.append(5)
# llist2.append(4)
# llist1.sumTwoLinkedLists(llist2)
#llist1.removeNthNodeFromLast(2)
#llist1.print_linkedlist()
#print(llist1.countOccurancesIterative(4))
#print(llist1.countOccurancesRecursive(llist1.head,4))
#llist2.print_linkedlist()#Creating a New Node
#llist1.mergeTwoSortedLinkedLists(llist2)
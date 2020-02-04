#Creating stack class and all the function/property stack has:
class Stack():
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def pop(self):
        return self.items.pop()
    def getStack(self):
        return self.items
        
        
def reverse_String_Using_Stack(stack,input_Str):
        for i in range(len(input_Str)):
            stack.push(input_Str[i])
        rev_str=""
        while not stack.is_empty():
            rev_str+=stack.pop()
        return rev_str
def reverse_String_Without_Stack(input_Str):
    return input_Str[::-1]
#Creating object for stack class
#s=Stack()
#Checking stack empty or not
#print(s.is_empty())
#Pushing value to the stack
#s.push("A")
#s.push("B")
#printing full stack
#print(s.getStack())
#s.push("C")
#print(s.getStack())
#Poping out value from stack
#s.pop()
#print(s.getStack())
#print(s.is_empty())
#Printing top of the stack
#print(s.peek())

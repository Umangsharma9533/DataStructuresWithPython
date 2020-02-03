#Import Stack class from the CreatingStack.py file
from CreatingStack import Stack
#define a function for comparing 2 character, Return True if both matches, False if no match
def is_match(top,paren):
    if top=='{' and paren=='}':
        return True
    if top=='[' and paren==']':
        return True
    if top=='(' and paren==')':
        return True
    else:
        return False
#Define a function to check whether string containing parenthesis is balanced or not
#Take string as the input and return True if balanced , False if not balanced
def isBalanced(paren_String):
    s=Stack()
    is_balanced=True
    index=0
    while index<len(paren_String) and is_balanced==True:
        paren=paren_String[index]
        if paren in "[{(":
            s.push(paren)
        else:
            top=s.pop()
            if not is_match(top,paren):
                is_balanced=False
        index+=1
    if s.is_empty() and is_balanced==True:
        return True
    else:
        return False
#Calling the funtion to check the result
#Print True if string is balanced
#Print False if string is not balanced
print(isBalanced("{{[([)]}}"))

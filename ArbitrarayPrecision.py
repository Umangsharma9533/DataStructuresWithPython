A=[]
n=int(input("ENter the number of index required"))
for i in range(0,n):
    ele=int(input())
    A.append(ele)
def arrayPrecision(A):
    A[-1]+=1
    for i in reversed(range(0,n)):
        if A[i]!=10:
            break
        A[i]=0
        A[i-1]+=1
        if A[0]==10:
            A[0]=1
            A.append(0)
arrayPrecision(A)
print(A)

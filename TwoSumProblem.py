A=[]
n=int(input("ENter the number of index required"))
for i in range(0,n):
    ele=int(input())
    A.append(ele)
def twoSumProblem(A,target):
    ht=dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(A[i],ht[A[i]])
            return True
        else:
            ht[target-A[i]]=A[i]
    return False
target=int(input("Enter the target"))
print(twoSumProblem(A,target))

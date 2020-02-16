A=[]
n=int(input("ENter the number of index required"))
for i in range(0,n):
    ele=int(input())
    A.append(ele)
#size complexity = O(n)
#time complexity = O(n)
def twoSumProblem(A,target):
    ht=dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(A[i],ht[A[i]])
            return True
        else:
            ht[target-A[i]]=A[i]
    return False
#Size=O(1)
#Time O(n)
def twoSumProblemOpt(A,target):
    i=0
    j=len(A)-1
    while i<=j:
        if (A[i]+A[j])==target:
            print(A[i],A[j])
            return True
        elif  (A[i]+A[j])<target:
            i+=1
        else:
            j-=1
    return False
target=int(input("Enter the target"))

print(twoSumProblem(A,target))

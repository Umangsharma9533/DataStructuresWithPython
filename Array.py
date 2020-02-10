def array_advance(A):
    further_reached=0
    last_idx=len(A)-1
    i=0
    while i<=further_reached and further_reached<last_idx:
        further_reached=max(further_reached,A[i]+i)
        i+=1
    return further_reached>=last_idx
A=[3,3,1,0,2,0,1]
B=[3,2,0,0,2,0,1]
print(array_advance(A))
print(array_advance(B))
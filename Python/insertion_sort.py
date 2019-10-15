def insertionsort(A):
    for i in range(1,len(A)):
        temp = A[i]
        k = i
        while k > 0 and temp < A[k-1]:
            A[k] = A[k-1]
            k -= 1
            A[k] = temp
A = [54,25,85,15,12,13,65,98]
insertionsort(A)
print("after the sorting A is",A)

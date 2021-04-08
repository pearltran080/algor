# Pearleen Tran
# CSC 321
# quick select

import sys
import random

def quickselect(A, k):
    k = int(k)
    if len(A) == 1:
        return A[0]
    else:
        
        p = random.randrange(len(A)) # random pivot index
        
        pivot = A[p]
        r = partition(A, p)

        if k < r:
            return quickselect(A[:r], k)
        elif k > r:
            return quickselect(A[r+1:len(A)], k-r-1)
        else:
            return A[r]

def partition(A, p):
    n = len(A)

    A[p],A[n-1] = A[n-1],A[p] # swap
    l = -1
    for i in range(n-1):
        if A[i] < A[n-1]:
            l+=1
            A[l],A[i] = A[i],A[l] # swap
    A[n-1],A[l+1] = A[l+1],A[n-1] # swap
    return l+1

def main():
    filename = sys.argv[1] # get file name

    file = open(filename)
    content = [eval(x) for x in file.read().split()]
    # read from file, split and convert to int
    
    print("The 4th smallest element is: {}".format(quickselect(content, 4)))
    print("The n/2th smallest element is: {}".format(quickselect(content, len(content)//2)))
    print("The n-1th smallest element is: {}".format(quickselect(content, len(content)-1)))

main()

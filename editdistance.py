# Pearleen Tran
# CSC 321

import sys

def EditDistance(A, B):
    oneRow = []
    for j in range(n):
        edit[0][j] = j
    
    for i in range(1, m):
        edit[i][0] = i
        for j in range(1,n):
            insert = (edit[i][j-1])+1
            delete = (edit[i-1][j])+1
            if A[i] == B[j]:
                replace = edit[i-1][j-1]
            else:
                replace = edit[i-1][j-1]+1
            edit[i][j] = min(insert,delete,replace)

    return edit[m-1][n-1]

# command line args
str1 = sys.argv[1]
str2 = sys.argv[2]
m = len(str1)
n = len(str2)

edit = []
for i in range(m):
    oneRow = []
    for j in range(n):
        oneRow.append(0)
    edit.append(oneRow)

print('Edit distance between {} and {} is {}'.format(str1, str2, EditDistance(str1, str2)))


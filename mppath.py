# Pearleen Tran
# CSC 321

def computeQ(q, p, N, d): # returns one row of input
    
    newLine = []
    newLine.append(0)
    pathNums = []

    for i in range(1, N+1):
        # access previous rows
        upperleft = q[i-1]
        above = q[i]
        upperright = q[i+1]

        if upperright > above and upperright > upperleft:
            pathNums.append(i+1)
        elif above > upperright and above > upperleft:
            pathNums.append(i)
        else:
            pathNums.append(i-1)
        
        newLine.append(max(upperleft, above, upperright) + p[i-1])

    newLine.append(0)
    
    return newLine, pathNums

def printPath(d, maxcolumn, n):
    s = []
    column = maxcolumn
    for row in range(n-1, -1, -1):
        s.append(column)
        column = d[row][column-1]

    for row in range(1, n+1):
        column = s.pop()
        print('({},{})'.format(row,column))

def main():
    
    # read from file
    file = open('ptable.txt')
    content = file.readlines()
    file.close()
    n = int(content.pop(0)) # save size

    # p table from input (fixed)
    pTable = []
    for i in content:
        line = i.split()
        read = []
        for j in line:
            read.append(int(j))
        pTable.append(read)

    # q table with first row filled with p[0] values
    qTable = [] # all rows
    tempQ = [] # single row
    tempQ.append(0)
    for k in pTable[0]:
        tempQ.append(k)
    tempQ.append(0)
    qTable.append(tempQ)

    # d table to track path w empty first row
    dTable = [] # all rows
    tempD = [] # single row
    for h in range(n):
        tempD.append(0)
    dTable.append(tempD)

    # fill in q table row by row
    for i in range(n-1):
        tableInput = computeQ(qTable[i], pTable[i+1], n, dTable[i])
        qTable.append(tableInput[0])
        dTable.append(tableInput[1])

    # find max of last row
    resultMax = 0
    resultPath = 0
    for j in range(1, n+1): # start from 1 to ignore padding
        if qTable[n-1][j] > resultMax:
            resultMax = qTable[n-1][j]
            resultPath = j
            
    print('The maximum profit is {}.'.format(resultMax))
    print('The maximum profit path is:')
    printPath(dTable, resultPath, n)

main()

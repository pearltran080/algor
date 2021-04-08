# Pearleen Tran
# CSC 321

def PlaceQueens(Q, r):
    if r >= len(Q):
        print(Q)
        return True
    else:
        for j in range(len(Q)):
            legal = True
            for i in range(r):
                # checking columns and diagonals
                if (Q[i]==j) or (Q[i]==j+(r-i)) or (Q[i]==j+(r+i)):
                    legal = False

            if (legal):
                Q[r] = j
                # call for next row
                PlaceQueens(Q, r+1)


def PlaceQueensF():
    # prompt for positive integer
    n = abs(int(input("Enter a # of Queens: ")))

    lst = []
    for k in range(n):
        lst.append(-1)

    # Last print is final board
    PlaceQueens(lst, 0)

PlaceQueensF()

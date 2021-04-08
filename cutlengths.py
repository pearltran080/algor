# Pearleen Tran
# CSC 321
# board cuts

def cutlengths (boardLen, allowed):
    print("Board length ", boardLen)
    print(f"{'Piece size':<15}{'Count'}")


    count = []
    remainingLen = boardLen
    for i in allowed:
        if (i <= remainingLen):
            cut = remainingLen//i
            #print("current cut length: {}, number of cuts {}".format(i, cut))
            remainingLen -= cut*i
            #print("remaining length after cut: {}".format(remainingLen))
            count.append(cut)
        else:
            count.append(0)

        # print current size and count for that size
        print(f"{'':<4}{i:<13}{count[-1]}")

    print("\n")

def main():
    #allowedLen = [20, 10, 5, 2, 1]
    allowedLen = [12, 9, 4, 3, 1]
    #cutlengths(99, allowedLen)
    #cutlengths(22, allowedLen)
    cutlengths(18, allowedLen)
    #cutlengths(33, allowedLen)

main()

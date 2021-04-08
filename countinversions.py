# Pearleen Tran
# CSC 321

def mergesort(array):
    if len(array) < 2:
        return array,0
    else:
        mid = (len(array) // 2)
        left = mergesort(array[:mid])
        right = mergesort(array[mid:])

        # left and right arrays
        result = merge (left[0], right[0])

        # array of result, inversion count of merged + left & right's count
        return result[0], result[1] + left[1] + right[1]

def merge (left, right):
    new = []
    a = 0
    b = 0
    count = 0
    while (a < len(left) and b < len(right)):
        if left[a] < right[b]:
            new.append(left[a])
            a+=1
        else:   # There are inversions
            new.append(right[b])
            b+=1
            count+=len(left) - a

    while a < len(left):    # All of right side elements have been copied
        new.append(left[a])
        a+=1
        
    while b < len(right):   # All of left side elements have been copied
        new.append(right[b])
        b+=1

    return new, count


file = open('inversionsinput.txt')
file = file.readlines()
lst = []
for i in file:
    lst.append(i)

    
print("This array contains {} inversions.".format(mergesort(lst)[1]))
#print the count

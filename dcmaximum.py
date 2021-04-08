# Pearleen Tran

def findMax (lst):
    if len(lst) == 1:
        return lst[0]
    else:
        mid = (len(lst)//2)
        left = findMax(lst[:mid])
        right = findMax(lst[mid:])

        result = maxOf (left,right)

        return result

def maxOf(left, right):
    if left >= right:
        return left
    return right


file = open('numbers.txt')
content = file.readlines()
file.close()

lst = []
for i in content:
    lst.append(eval(i))

print(findMax(lst))

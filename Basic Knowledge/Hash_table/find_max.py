items = [6, 20, 98, 19, 56, 23, 87, 41, 49, 53]

def fm(items):

    if len(items) == 1:         # Breaking condition - if there is only one element in list
        return items[0]
    
    op1 = items[0]              # These two lines make the algorithm go in reverse direction as function will call itself until there is only two items left in the list to give the comparision result
    op2 = fm(items[1:])

    if op1 > op2:
        return op1
    else:
        return op2

print(fm(items))
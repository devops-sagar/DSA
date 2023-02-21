order_list = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
un_order_list = [3, 66, 23, 11, 6, 0, 28, 95, 22, 1]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # calculate the middle point
        midPt = (lowerIdx + upperIdx)// 2

        # if item is found, return the index
        if itemlist[midPt] == item:
            return midPt
        # otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, order_list))
print(binarysearch(87, order_list))
print(binarysearch(250, order_list))
print(binarysearch(66, un_order_list))
print(binarysearch(250, un_order_list))
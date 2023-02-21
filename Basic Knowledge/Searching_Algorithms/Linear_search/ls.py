un_order_list = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
order_list = [156, 234, 378, 456, 589, 645, 7, 856, 967]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i
    
    return None


print(find_item(87, un_order_list))
print(find_item(250, un_order_list))
print(find_item(7, order_list))
print(find_item(967, order_list))
# Script to find if the given list is sorted or not

order_list = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
un_order_list = [3, 66, 23, 11, 6, 0, 28, 95, 22, 1]

def sorted(data):

    # for i in range(0, len(data)-1):         # BruteForce Solution (something comman which required more time and space complexity)
    #     if (data[i] > data[i+1]):
    #         return False
    # return True

    return all(data[i] <= data[i+1] for i in range(len(data) - 1))      # otimized solution with better time and space complexity

print(sorted(order_list))
print(sorted(un_order_list))
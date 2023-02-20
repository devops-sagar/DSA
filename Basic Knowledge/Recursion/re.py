''' ************************************************************************
Start of simple Implementation - just to show how recursion works
************************************************************************'''
# def countdown(x):
#     if (x == 0):
#         print("DOneeeee")
#         # return
#     else:
#         print(x, "...")
#         countdown(x-1)
#         print("ok")
# countdown(5)
''' ************************************************************************
end of simple Implementation - just to show how recursion works
************************************************************************'''



def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        # return num**pwr
        return num * power(num, pwr-1)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))

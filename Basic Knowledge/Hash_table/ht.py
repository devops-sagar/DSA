my_list = ["Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Ball","Ball","Ball","Ball","Ball","Ball","Ball","Ball","Ball","Ball","Car","Car","Car","Car","Car","Car","Car","Car","Car","Car","Car","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Elephant","Elephant","Elephant","Elephant","Elephant","Elephant","Elephant","Elephant","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","grounfhog","groundhog"] # Time Complexity : O(n) due to linear fashion checking of items


filter = dict()         # Crearing empty dictionar as Keys in the dictionary doesn't repeat itself

''' ************************************************************************
Algorithm to filter out the unique items in the given list - Items with the multiple occurance will convert to one occurance - START
************************************************************************'''

# for item in my_list:
#     filter[item] = 0

# # result = set(filter.keys())           # using the walrus operator (:=) these two lines can be converted to one
# # print(result)

# print(result := set(filter.keys()))     # Using the walrus operator

''' ************************************************************************
Algorithm to filter out the unique items in the given list - Items with the multiple occurance will convert to one occurance - END
************************************************************************'''

''' ************************************************************************
Algorithm to count the filter outed unique items in the given list - START
************************************************************************'''

for item in my_list:
    if item in filter.keys():
        filter[item] += 1
    else:
        filter[item] = 1

print(filter)

''' ************************************************************************
Algorithm to count the filter outed unique items in the given list - END
************************************************************************'''

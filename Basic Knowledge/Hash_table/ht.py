# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print("\nDictionary with the use of Integer Keys: ")
# print(Dict)

# Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
# print("\nDictionary with the use of Mixed Keys: ")
# print(Dict)

''' ************************************************************************
Algorithm to filter out the unique items in the given list - Items with the multiple occurance will convert to one occurance - START
************************************************************************'''

my_list = ["Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Apple","Ball","Ball","Ball","Ball","Ball","Ball","Ball","Ball","Ball","Ball","Car","Car","Car","Car","Car","Car","Car","Car","Car","Car","Car","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Dog","Elephant","Elephant","Elephant","Elephant","Elephant","Elephant","Elephant","Elephant","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Frog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","Grounfhog","grounfhog","groundhog"]

filter = dict()         # Crearing empty dictionar as Keys in the dictionary doesn't repeat itself

for item in my_list:
    filter[item] = 0

# result = set(filter.keys())           # using the walrus operator (:=) these two lines can be converted to one
# print(result)

print(result := set(filter.keys()))     # Using the walrus operator

''' ************************************************************************
Algorithm to filter out the unique items in the given list - Items with the multiple occurance will convert to one occurance - END
************************************************************************'''
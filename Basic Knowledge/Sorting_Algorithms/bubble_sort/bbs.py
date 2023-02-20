x = [81,62,93,74,45]

for i in range (len(x)-1, 0, -1):   # if you see nested for loops, that's the clear indication of infamous O(n^2) complexity
    for j in range (i):             # you must avoid this type of structure in Algorithms
        if x[j] > x[j+1]:
            print(f"Comparing Between {x[j]} and {x[j+1]}")
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            print(f"Swiped elements {x[j]} and {x[j+1]}")
    print(x)
x = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesrt(data):
    if len(data) > 1:
        mid = len(data) // 2
        leftarr = data[:mid]
        rightarr = data[mid:]

        mergesrt(leftarr)       # Using Recursion Here
        mergesrt(rightarr)      # Using Recursion Here

        i = j = k = 0           # Index into left, right and merge_array respectively

        while i < len(leftarr) and j < len(rightarr):

            if leftarr[i] < rightarr[j]:        # Comparing left section element and right section element just like I provide in drawing
                data[k] = leftarr[i]            # Merge index accepting left index element
                i += 1                          # increasing Left index upon successful comparision
            else:
                data[k] = rightarr[j]           # Merge index accepting right index element
                j += 1                          # increasing Right index upon unsuccessful comparision
            k += 1                              # increasing merge index position to allow the space

        while i < len(leftarr):                 # Even after if some elements are left behind wich are already sorted in left array, assigning them to merge index
            data[k] = leftarr[i]
            i += 1
            k += 1
        while j < len(rightarr):                # Even after if some elements are left behind wich are already sorted in right array, assigning them to merge index
            data[k] = rightarr[j]
            j += 1
            k += 1

print(f"Items before sorting: {x}")
mergesrt(x)                                     
print(f"Items after sorting: {x}")
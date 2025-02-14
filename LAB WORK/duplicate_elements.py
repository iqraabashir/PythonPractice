arr = [1, 2, 3, 4, 1, 2, 4, 6, 8, 8]
print("Duplicate elements in the array are: ")
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            print(arr[j])

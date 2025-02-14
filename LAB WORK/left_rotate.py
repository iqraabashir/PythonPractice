arr = [1, 2, 3, 4, 5]
n = int(input("Enter the number of positions to rotate: "))
print("Original array: ", arr)
#[3, 4, 5] + [1, 2]
arr = arr[n:] + arr[:n]
print("Array after left rotation: ", arr)

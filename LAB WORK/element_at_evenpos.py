arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Elements at even position: ")
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i] , end = " ")
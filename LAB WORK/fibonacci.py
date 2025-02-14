# def fibonacci(n):
#     fib_sequence = [0, 1]
#     while len(fib_sequence) < n:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence

n = int(input("Enter The Number Of Terms: "))
a = 0
b = 1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    print("Fibonacci sequence:" , end=" ")
    for i in range(n):
      print(a, end = " ")
      a, b = b, a+b


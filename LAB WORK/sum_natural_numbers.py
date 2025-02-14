# def sum_of_natural_numbers(n):
#     return n * (n + 1) // 2

# n = int(input("Enter a number: "))
# if n < 0:
#     print("Enter a positive number.")
# else:
#     sum = n * (n + 1) // 2
#     print("Sum of natural numbers up to", n, "is:", sum)
    
    # print("Sum of natural numbers up to", n, "is:", sum_of_natural_numbers(n))

def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

n = int(input("Enter a number: "))
if n < 0:
    print("Enter a positive number.")
else:
    sum = sum_of_natural_numbers(n)
    print("Sum of natural numbers up to", n, "is:", sum)
    
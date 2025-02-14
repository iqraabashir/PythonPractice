# def list_to_string(lst):
#     return ' '.join(map(str, lst))

# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# print(list_to_string(my_list))

list = ['hello', 'world', 'python', 'is', 'fun']
result = ' '.join(list)
print(result)
print("Type of list: ", type(list))
print("Type of result: ", type(result)) 


numbers = [1, 2, 3, 4, 5]
result = ' '.join(map(str, numbers))
print(result)
print("Type of numbers: ", type(numbers))
print("Type of result: ", type(result))


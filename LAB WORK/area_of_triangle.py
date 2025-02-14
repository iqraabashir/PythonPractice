# def calculate_triangle_area(base, height):
#     return 0.5 * base * height

# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# area = calculate_triangle_area(base, height)
# print("Area of the triangle with base", base, "and height", height, "is:", area)

# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# area = 0.5 * base * height
# print("Area of the triangle with base", base, "and height", height, "is:", area)

#using heron's formula
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the triangle with sides", a, b, c, "is:", area)


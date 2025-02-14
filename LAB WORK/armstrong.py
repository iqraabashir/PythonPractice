num = int(input("Enter a number: "))
# checking length of the number
len = len(str(num))
# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
#checking if the number is negative
while temp > 0:
   #taking the last digit of the number
   digit = temp % 10
   #adding the cube of the digit to the sum
   sum = sum + digit ** len
   # sum += digit ** len
   #removing the last digit from the number
   temp = temp // 10
   # temp //= 10

# display the result 
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
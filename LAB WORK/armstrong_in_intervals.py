lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
for num in range(lower, upper + 1): 
   # length of number
   length = len(str(num))   
   # initialize sum
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** length
       temp //= 10
# display the result
   if num == sum:
       print(num)

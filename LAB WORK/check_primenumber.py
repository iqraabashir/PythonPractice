num = int(input("enter the number: "))

if num < 2:
    print(num, "is not a prime number")
else:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
        #    print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
         
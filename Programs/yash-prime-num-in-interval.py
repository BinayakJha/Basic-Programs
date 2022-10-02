# Python program to display all the prime numbers within an interval

lower = int(input("Enter lower bound"))
upper = int(input("Enter upper bound"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

def recursum(n):
   if n <= 1:
       return n
   else:
       return n + recursum(n-1)

num = 16

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recursum(num))
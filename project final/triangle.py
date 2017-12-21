import math
def triangle():
   n=int(raw_input("Enter the Number : "))

   for i in range(0,n+1):
      print ""
      for j in range(0,i+1):
           a=math.factorial(i)/(math.factorial(i-j)*math.factorial(j))
           if a%2==1:
               print "X",
           else:
               print " ",

import random
print """The Rules Are:
If you win : You get 4% of your money initial bet
If you lose : You get 1% of your money initial bet
All The Best!"""

mypot = float(input("Please enter the amount of money you want to bet: "))

a=mypot/100
b="y"
while b.lower()=="y":
    d1 = random.randint(1,6)          #First Diceroll
    d2 = random.randint(1,6)          #Second Diceroll
    sum=d1+d2
    if mypot > 0:
        if sum == 7:
            print "First Diceroll ---> ",d1
            print "Second Diceroll ---> ",d2
            print "Your roll was a 7 you earned",4*a
            print "Balance:", mypot+(4*a)
            b=raw_input("Play Again? (Y/N)")
            mypot+=(4*a)
            
        else:
            print "First Diceroll ---> ",d1
            print "Second Diceroll ---> ",d2
            print "Sorry you did not roll a 7"
            print "Balance:", mypot - a
            b=raw_input("Play Again? (Y/N)")
            mypot-=a
            
    else:
        print "Sorry you do not have no more money in your pot"
        break

print "Thank You for Playing"
    

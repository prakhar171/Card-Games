from turtle import *
import Tkinter as logo
import webbrowser
import blackjack
import lucky7
import triangle
import diamond

print "Check out our logo "
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

root = logo.Tk()
lbl = logo.Button(root, text=r"Social.html", fg="black", cursor="arrow")
lbl.pack()
lbl.bind("<Button-1>", callback)
root.mainloop()


pen1=Pen()
pen2=Pen()

pen1.screen.bgcolor("#B51108")

pen1.color("#FFFFFF")
pen2.color("#532222")

pen2.up()
pen2.goto(-50,50)
pen2.down()
pen1.begin_fill()
pen1.circle(100)
pen1.end_fill()
pen2.write("KP",font=('Candara',70))

pen1.up()
pen1.goto(-250,-150)
pen1.down()
pen1.write("""1. Blackjack
2. Lucky 7
3. Pattern 1
4. Pattern 2""",font=("Candara",20))

while True:
    k=input('Enter Choice ') 
    if k==1:
        blackjack.blackjack()
    elif k==2:
        lucky7.lucky7()
    elif k==3:
        triangle.triangle()
    else:
        diamond.diamond()
    print ""
    x=raw_input('You want to continue here (y/n)? ')
    if x=='n':
        print "Thank You For Playing"
        break
    else:
        True
